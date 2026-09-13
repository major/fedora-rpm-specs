%global forgeurl https://github.com/sherlock-project/sherlock
Version:        0.16.2
%forgemeta
Name:           sherlock-project
Release:        %autorelease
Summary:        Hunt down social media accounts by username across social networks
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  help2man
BuildRequires:  python3-devel

%global _description %{expand:
Hunt down social media accounts by username across 400+ social networks and
websites. New targets are tested and implemented regularly.}

%description %{_description}


%prep
%forgeautosetup -v

%generate_buildrequires
# Relax requirements on pandas, since Fedora Rawhide has newer versions
sed -i 's/pandas = "\^2.2.1"/pandas = ">=2.2.1"/' pyproject.toml
%pyproject_buildrequires -t


%build
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
