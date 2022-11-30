Name:           python-userpath
Version:        1.8.0
Release:        %autorelease
Summary:        Cross-platform tool for adding locations to the user PATH

# SPDX
License:        MIT
URL:            https://github.com/ofek/userpath
Source0:        %{pypi_source userpath}

# Man pages in groff_man(7) format hand-written for Fedora based on --help
# output.
Source10:       userpath.1
Source11:       userpath-append.1
Source12:       userpath-prepend.1
Source13:       userpath-verify.1

BuildArch:      noarch

BuildRequires:  python3-devel
# RHBZ#1985340, RHBZ#2076994
BuildRequires:  pyproject-rpm-macros >= 1.2.0

%global common_description %{expand:
Cross-platform tool for adding locations to the user PATH, no elevated
privileges required!}

%description %common_description


%package -n     python3-userpath
Summary:        %{summary}

%description -n python3-userpath %common_description


%prep
%autosetup -n userpath-%{version}

# Dev requirements include test requirements; but we want to filter out
# coverage, linting, etc.
sed -r '/^(coverage)$/d' requirements-dev.txt > requirements-dev.filtered.txt


%generate_buildrequires
%pyproject_buildrequires requirements-dev.filtered.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files userpath

install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check
# We use pytest directly, since the only contribution of the tox configuration
# is adding coverage analysis—which we do not want.
%pytest


%files -n python3-userpath -f %{pyproject_files}
%license LICENSE.txt
%doc HISTORY.rst
%doc README.md

%{_bindir}/userpath
%{_mandir}/man1/userpath*.1*


%changelog
%autochangelog
