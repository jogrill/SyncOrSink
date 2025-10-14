# In Sync or Sink? Analyzing Tactical Divides between Attackers and Defenders

## Abstract

Attackers and defenders are in a constant race – while defenders must secure everything, attackers only need to exploit a single
vulnerability. For organizations, having effective cybersecurity processes and playbooks is crucial. But how can they be sure they
are truly prepared? To guide them, we analyze more than one hundred and seventy thousand (172,351) documented vulnerabilities,
identifying the attack tactics and techniques commonly used by adversaries. We also examine and map 1,362 cybersecurity
playbooks to highlight the defensive tactics and techniques most frequently recommended by Security Orchestration, Automation,
and Response (SOAR) vendors. By aligning these two perspectives, we offer a comparison between attackers’ and defenders’
capabilities. Our findings reveal that tactics like Execution, Defense Evasion, and Impact dominate the vulnerability landscape.
Cybersecurity playbooks focus heavily on attacker detection while missing opportunities in defensive tactics like hardening systems
or deceiving attackers, and also neglecting key defensive techniques to effectively counter observed attacker behavior. This
misalignment has significant implications: Organizations should adjust their defense strategies to align with our proposed playbook
use cases, while SOAR vendors need to broaden their playbook offerings to guide organizations. As it stands, defenders remain
closer to sinking than staying in sync.

### Usage

1. **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```

2. **Open the notebook**:
    Navigate to the  notebooks `01_Attacker_Analysis.ipynb` and `02_Defender_Analysis.ipynb`.

3. **Explore and analyze the data**:
    Follow the steps in the notebook to explore, process, and analyze the CVE and playbook data.
