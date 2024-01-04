%bcond_without tests

%global _description %{expand:
Helper module to easily develop special remotes for git annex. AnnexRemote
handles all the protocol stuff for you, so you can focus on the remote itself.
It implements the complete external special remote protocol and fulfils all
specifications regarding whitespaces etc. This is ensured by an excessive test
suite. Extensions to the protocol are normally added within hours after they
have been published.}

%global forgeurl https://github.com/Lykos153/AnnexRemote

Name:           python-annexremote
Version:        1.6.4
Release:        %autorelease
Summary:        Git annex special remotes made easy

%forgemeta

License:        GPL-3.0-only
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

%description %_description

%package -n python3-annexremote
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-annexremote %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%forgesetup

# Remove shebang
sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' examples/git-annex-remote-directory
chmod -x examples/git-annex-remote-directory

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires %{?with_tests:-x test}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l annexremote

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_check_import

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
