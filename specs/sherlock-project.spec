%global forgeurl https://github.com/sherlock-project/sherlock
Version:        0.16.0
%forgemeta
Name:           sherlock-project
Release:        %autorelease
Summary:        Hunt down social media accounts by username across social networks
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

Patch0:         0001-Remove-tor.patch

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel

%global _description %{expand:
Hunt down social media accounts by username across 400+ social networks and
websites. New targets are tested and implemented regularly.}

%description %{_description}


%prep
%forgeautosetup -p1
sed -i '/torrequest/d' 'pyproject.toml' # Pending upstream removal

%generate_buildrequires
# Relax requirements on pandas and requests, since Fedora Rawhide has newer versions
# Also remove torrequest since we patch out tor.
sed -i 's/pandas = "\^2.2.1"/pandas = ">=2.2.1"/' pyproject.toml
%pyproject_buildrequires -t


%build
# Project now uses Poetry and dynamic versioning, so pyproject version is 0
# __init__ is currently the single source of truth for version info
sherlock_version=$(sed -n 's/^__version__ *= *"\([0-9.]*\)"/\1/p' sherlock_project/__init__.py)
sed -r -i "s/^version *= .*?$/version = \"$sherlock_version\"/" pyproject.toml
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L sherlock_project

sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock_project/__main__.py'
sed -r -i '1{/^#!/d}' '%{buildroot}%{python3_sitelib}/sherlock_project/sherlock.py'

install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --name='%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/sherlock.1' \
    '%{buildroot}%{_bindir}/sherlock'


%check
%tox -e offline


%files -f %{pyproject_files}
%license LICENSE
%doc docs/README.md
%{_bindir}/sherlock
%{_mandir}/man1/sherlock.1*


%changelog
%autochangelog
