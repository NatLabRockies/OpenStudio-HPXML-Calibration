import glob
import os
import shutil
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: run_ci_simulations.py job_num")

    SKIP_FILENAMES = (
        "ihmh6.xml",  # Missing natural gas consumption data
        "ihmh7.xml",  # Has PV
        "house02.xml",  # Missing natural gas consumption data
        "house05.xml",  # Missing natural gas consumption data
        "house09.xml",  # Missing natural gas consumption data
        "house10.xml",  # Missing natural gas consumption data
        "house22.xml",  # Gap in electricity consumption data
        "house31.xml",  # Gap in electricity consumption data
        "house32.xml",  # Electricity consumption covers less than 300 days
        "house37.xml",  # Electricity consumption covers less than 300 days
        "house44.xml",  # Missing electricity consumption data
        "house45.xml",  # Missing electricity consumption data
        "house46.xml",  # Zeroes in electricity consumption data
        "house50.xml",  # Billing period shorter than 20 days
        "house57.xml",  # Natural gas consumption covers less than 300 days
        "house77.xml",  # Billing period shorter than 20 days
        "house83.xml",  # Natural gas consumption covers less than 300 days
        "house85.xml",  # Missing fuel oil consumption data
        "house86.xml",  # Missing fuel oil consumption data
    )

    root_dir = Path(__file__).resolve().parent.parent
    test_hpxmls_dir = root_dir / "test_hpxmls"
    tests_dir = root_dir / "tests"
    top_output_dir = tests_dir / "all_calibration_results"

    shutil.rmtree(top_output_dir, ignore_errors=True)

    all_xmls = []
    for xml in glob.glob("**/*.xml", root_dir=test_hpxmls_dir, recursive=True):
        if "invalid_homes" in xml:
            continue

        if os.path.basename(xml) in SKIP_FILENAMES:
            continue

        all_xmls.append(xml)

    # Split simulations across 4 CI jobs
    num_jobs = 4
    num_files = -(-len(all_xmls) // num_jobs)
    job_num = int(sys.argv[1])
    job_xmls = [all_xmls[i : i + num_files] for i in range(0, len(all_xmls), num_files)][job_num]

    for xml in job_xmls:
        print(f"CALIBRATING {xml}...")
        output_dir = top_output_dir / Path(xml).stem

        subprocess.run(
            [
                "uv",
                "run",
                "openstudio-hpxml-calibration",
                "calibrate",
                "--hpxml-filepath",
                str(test_hpxmls_dir / xml),
                "--output-dir",
                str(output_dir),
                "--config-filepath",
                str(tests_dir / "data" / "test_config_for_ci_calibrations.yaml"),
                "--num-proc",
                "8",
                "--verbose",
                "--verbose",
            ],
            check=True,
        )
