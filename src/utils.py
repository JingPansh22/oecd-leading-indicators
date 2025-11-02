# utils.py
# --------------------------------------------
# Utility module for managing project paths
# --------------------------------------------
# This script automatically detects the project root,
# sets up standard directories for data, figures, and tables,
# and provides helper functions to simplify file path handling.


from pathlib import Path

# Define project root (go one level up from /src)
ROOT = Path(__file__).resolve().parents[1]

# Define key directories
DATA = ROOT / "data" / "oecd"          # Raw and cleaned data files
FIGS = ROOT / "figs"                   # Visualization output directory
TABLES = ROOT / "reports" / "tables"   # Analytical tables output directory

# Ensure all required folders exist (auto-create if missing)
for p in (DATA, FIGS, TABLES):
    p.mkdir(parents=True, exist_ok=True)

# Helper functions for saving outputs with unified paths
def p_fig(name: str) -> Path:
    """
    Returns a full path under the 'figs' directory for saving figures.
    Example:
        plt.savefig(p_fig("trend_us.png"))
    """
    return FIGS / name

def p_tab(name: str) -> Path:
    """
    Returns a full path under the 'reports/tables' directory for saving CSV tables.
    Example:
        df.to_csv(p_tab("summary.csv"), index=False)
    """
    return TABLES / name

