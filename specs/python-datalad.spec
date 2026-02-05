# require network, so disabled by default
# to run on mock, use --enable-network
# only a couple of tests fail
%bcond_with tests

%global forgeurl https://github.com/datalad/datalad

Name:           python-datalad
Version:        1.3.1
%global tag     %{version}
%forgemeta
Release:        %autorelease
Summary:        Keep code, data, containers under control with git and git-annex

# spdx verified
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%global _description %{expand:
DataLad makes data management and data distribution more accessible. To do
that, it stands on the shoulders of Git and Git-annex to deliver a
decentralized system for data exchange. This includes automated ingestion of
data from online portals and exposing it in readily usable form as Git(-annex)
repositories, so-called datasets. The actual data storage and permission
management, however, remains with the original data providers.

The full documentation is available at https://docs.datalad.org and
https://handbook.datalad.org provides a hands-on crash-course on DataLad

Extensions:

A number of extensions are available that provide additional functionality for
DataLad. Extensions are separate packages that are to be installed in addition
to DataLad. In order to install DataLad customized for a particular domain, one
can simply install an extension directly, and DataLad itself will be
automatically installed with it. An annotated list of extensions is available
in the DataLad handbook.

Support:

The documentation for this project is found here: https://docs.datalad.org

If you have a problem or would like to ask a question about how to use DataLad,
please submit a question to NeuroStars.org with a datalad tag. NeuroStars.org
is a platform similar to StackOverflow but dedicated to neuroinformatics.

All previous DataLad questions are available here:
https://neurostars.org/tags/datalad/}

%description %_description

%package -n python3-datalad
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  git-core
BuildRequires:  git-annex
# for 7za
BuildRequires:  p7zip
BuildRequires:  p7zip-plugins
# Not added automatically
Requires:       git-annex
Requires:       p7zip p7zip-plugins
Provides:       datalad = %{version}-%{release}

%description -n python3-datalad %_description

%prep
%forgesetup

# tweak test requirements
# - remove type packages
# - remove mypy
# - remove pytest-fail-slow
sed -i -e '/types-python-dateutil/ d' \
    -e '/types-requests/ d' \
    -e '/mypy/ d' \
    -e '/pytest-fail-slow/ d' \
    setup.py

# Do not read deps from tox.ini, just use setup.py
# tox.ini calls requirements.txt which doesn't work
rm -f tox.ini

%if %{fedora} <= 42
# correct license declaration: errors on F42
sed -i -e '/^license/ d' pyproject.toml
%endif

# Correct shebangs in tools
find . -type f -exec sed -i "s|#!/usr/bin/env.*python$|#!%{python3}|" '{}' ';'

# remove shebangs
find datalad/resources/procedures/ -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# required for tests, and man page generation
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"

%if %{with tests}
# Tests wants a git repo
git init .
git add .
git commit -m "Dummy commit"

# correct function argument auto_spec -> autospec
sed -i 's/auto_spec/autospec/' datalad/support/tests/test_annexrepo.py
%endif

%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-x tests}

%build
%pyproject_wheel
# build man pages
%{python3} setup.py build_manpage

%install
%pyproject_install
%pyproject_save_files datalad

# install man pages
install -m 0644 -p -Dt $RPM_BUILD_ROOT/%{_mandir}/man1/  build/man/*.1


%check
%if %{with tests}
export PATH="${PATH}:%{buildroot}/%{_bindir}"
%pytest
%endif
# check import
# exclude imports that require a dataset
%pyproject_check_import -e *test* -e *cfg_text2git* -e *cfg_yoda*

%files -n python3-datalad -f %{pyproject_files}
%doc README.md CONTRIBUTORS CONTRIBUTING.md CHANGELOG.md CODE_OF_CONDUCT.md
%{_bindir}/datalad
%{_bindir}/git-annex-remote-datalad
%{_bindir}/git-annex-remote-datalad-archives
%{_bindir}/git-annex-remote-ora
%{_bindir}/git-annex-remote-ria
%{_bindir}/git-credential-datalad
%{_mandir}/man1/*.1*

%changelog
%autochangelog
