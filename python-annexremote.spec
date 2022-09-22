%bcond_without tests

%global _description %{expand:
Helper module to easily develop special remotes for git annex. AnnexRemote
handles all the protocol stuff for you, so you can focus on the remote itself.
It implements the complete external special remote protocol and fulfils all
specifications regarding whitespaces etc. This is ensured by an excessive test
suite. Extensions to the protocol are normally added within hours after they
have been published.}


Name:           python-annexremote
Version:        1.6.0
Release:        %autorelease
Summary:        Git annex special remotes made easy

# https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses
License:        GPLv3
URL:            https://pypi.org/pypi/annexremote
Source0:        %{pypi_source annexremote}

# Update the assertion error strings
# Sent upstream: https://github.com/Lykos153/AnnexRemote/pull/29
# Required for Py3.10 (F35+)
Patch0:         0001-fix-update-assertion-error-text.patch

BuildArch:      noarch

%description %_description

%package -n python3-annexremote
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  git-core

%description -n python3-annexremote %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%if 0%{?fedora} >= 35
%autosetup -n annexremote-%{version} -S git
%else
%autosetup -n annexremote-%{version} -N
%endif

# Replace nose with pytest
sed -i "s/'nose'/'pytest'/" setup.py
sed -i 's/    def Test/    def test_/' tests/test_*.py

# Remove shebang
sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' examples/git-annex-remote-directory
chmod -x examples/git-annex-remote-directory

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files annexremote

%check
# Basic import check test
%py3_check_import annexremote

%if %{with tests}
%{pytest}
%endif

%files -n python3-annexremote -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc docs/annexremote examples

%changelog
%autochangelog
