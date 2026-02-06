%global _description %{expand:
Advanced Python Scheduler (APScheduler) is a Python library that lets you
schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.}

Name:           python-APScheduler
Version:        3.11.2
Release:        %autorelease
Summary:        In-process task scheduler with Cron-like capabilities

License:        MIT
URL:            https://pypi.org/project/APScheduler/
Source0:        %{pypi_source apscheduler}
BuildArch:      noarch

%description %_description

%package -n python3-APScheduler
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-APScheduler %_description

%prep
%autosetup -n apscheduler-%{version} -p1
# Remove that test as it require services (redis, zookeeper, ...)
# up and running. Upstream provides a docker compose to spawn
# services before running these tests.
rm tests/test_jobstores.py
# Skip missing dependency in Fedora 43
sed -i 's/,rethinkdb//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test -x tornado

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files apscheduler

%check
# Default timezone to UTC otherwise unit tests fail.
export TZ=UTC
%pytest

%files -n python3-APScheduler -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
