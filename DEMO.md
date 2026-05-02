# Bazaarly — Seeded Findings (26 total)

## SAST (11)
| ID | CWE | File |
|---|---|---|
| BAZ-SAST-001 | CWE-89   | `bazaarly/orders/views.py` (raw SQL via `.raw()`) |
| BAZ-SAST-002 | CWE-1336 | `bazaarly/marketing/views.py` (Django template SSTI) |
| BAZ-SAST-003 | CWE-915  | `bazaarly/orders/views.py` (mass assignment via `**request.POST`) |
| BAZ-SAST-004 | CWE-798  | `bazaarly/settings.py` (hardcoded SECRET_KEY, Stripe key) |
| BAZ-SAST-005 | CWE-489  | `bazaarly/settings.py` (DEBUG=True, ALLOWED_HOSTS=['*']) |
| BAZ-SAST-006 | CWE-79   | `bazaarly/templates/cart.html` (`\|safe` on user content) |
| BAZ-SAST-007 | CWE-22   | `bazaarly/orders/exports.py` (path traversal on filename) |
| BAZ-SAST-008 | CWE-918  | `bazaarly/orders/webhooks.py` (SSRF via requests.get) |
| BAZ-SAST-009 | CWE-352  | `bazaarly/admin/views.py` (`@csrf_exempt` on state-changing route) |
| BAZ-SAST-010 | CWE-327  | `bazaarly/auth/passwords.py` (SHA1 password hashing) |
| BAZ-SAST-011 | CWE-209  | `bazaarly/middleware.py` (DEBUG=True returns full traceback) |

## IaC (6)
- BAZ-IAC-001 GCS bucket `iam_member: allUsers viewer` (`infra/terraform/gcs.tf`)
- BAZ-IAC-002 Cloud SQL `authorized_networks: 0.0.0.0/0` (`infra/terraform/sql.tf`)
- BAZ-IAC-003 Cloud SQL no SSL required (`infra/terraform/sql.tf`)
- BAZ-IAC-004 Container runs as root (`Dockerfile`)
- BAZ-IAC-005 K8s Service type LoadBalancer with no NetworkPolicy (`infra/k8s/service.yaml`)
- BAZ-IAC-006 K8s container `allowPrivilegeEscalation: true` (`infra/k8s/deployment.yaml`)

## SCA (5)
| ID | Package | Version | CVE |
|---|---|---|---|
| BAZ-SCA-001 | Django                | 3.2.4   | CVE-2021-35042 |
| BAZ-SCA-002 | Pillow                | 8.0.1   | CVE-2021-25287 |
| BAZ-SCA-003 | requests              | 2.20.0  | CVE-2023-32681 |
| BAZ-SCA-004 | sqlparse              | 0.4.1   | CVE-2021-32839 |
| BAZ-SCA-005 | celery                | 4.4.0   | CVE-2021-23727 |

## Pipeline (4)
- BAZ-CI-001 Hardcoded GCP service-account JSON in env (`.github/workflows/ci.yml`)
- BAZ-CI-002 `actions/checkout@v3` plus `pull_request_target` + checkout head ref
- BAZ-CI-003 No `permissions:` block
- BAZ-CI-004 `pip install` from a non-pinned, mutable `requirements.txt` URL fetched at build time
