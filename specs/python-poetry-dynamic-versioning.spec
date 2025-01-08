# tests require network to use poetry
%bcond tests 0

%global _description %{expand:
This is a Python 3.7+ plugin for Poetry 1.2.0+ and Poetry Core 1.0.0+ to enable
dynamic versioning based on tags in your version control system, powered by
Dunamai. Many different version control systems are supported, including Git
and Mercurial; please refer to the Dunamai page for the full list (and minimum
supported version where applicable).

poetry-dynamic-versioning provides a build backend that patches Poetry Core to
enable the versioning system in PEP 517 build frontends. When installed with
the plugin feature (i.e., poetry-dynamic-versioning[plugin]), it also
integrates with the Poetry CLI to trigger the versioning in commands like
poetry build.}

Name:           python-poetry-dynamic-versioning
Version:        1.5.0
Release:        %{autorelease}
Summary:        Plugin for Poetry to enable dynamic versioning based on VCS tags

# SPDX
License:        MIT
URL:            https://github.com/mtkennerly/poetry-dynamic-versioning
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description %_description

%package -n python3-poetry-dynamic-versioning
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  help2man

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/hg
BuildRequires:  /usr/bin/darcs
BuildRequires:  /usr/bin/svn
BuildRequires:  /usr/bin/bzr
BuildRequires:  /usr/bin/fossil
BuildRequires:  /usr/bin/poetry
# pijul is not in Fedora yet
#BuildRequires:  /usr/bin/pijul
%endif

%description -n python3-poetry-dynamic-versioning %_description

%prep
%autosetup -n poetry-dynamic-versioning-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files poetry_dynamic_versioning
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 \
    docs/poetry-dynamic-versioning.1

%check
%if %{with tests}
# set up git
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
# set up bzr
brz whoami "Your Name <name@example.com>"
# set up darcs
export DARCS_EMAIL="Yep something <name@example.com>"

%{pytest}
%endif

%files -n python3-poetry-dynamic-versioning -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md README.plugin.md
%{_bindir}/poetry-dynamic-versioning
%{_mandir}/man1/poetry-dynamic-versioning.1*

%changelog
%autochangelog
