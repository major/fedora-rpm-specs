Name:           python-userpath
Version:        1.9.2
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

BuildSystem:    pyproject
BuildOption(generate_buildrequires): requirements-dev.txt
BuildOption(install): --assert-license userpath

%global common_description %{expand:
Cross-platform tool for adding locations to the user PATH, no elevated
privileges required!}

%description %common_description


%package -n     python3-userpath
Summary:        %{summary}

%description -n python3-userpath %common_description


%prep -a
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency coverage:ignore


%install -a
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_mandir}/man1' \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'


%check -a
# We use pytest directly, since the only contribution of the tox configuration
# is adding coverage analysis—which we do not want.
%pytest


%files -n python3-userpath -f %{pyproject_files}
%doc HISTORY.rst
%doc README.md

%{_bindir}/userpath
%{_mandir}/man1/userpath*.1*


%changelog
%autochangelog
