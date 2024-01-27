Name:           thefuck
Version:        3.32
Release:        %autorelease
Summary:        App that corrects your previous console command
License:        MIT
URL:            https://github.com/nvbn/thefuck
Source0:        https://github.com/nvbn/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# https://github.com/nvbn/thefuck/issues/1381
%if v"0%{?python3_version}" >= v"3.12"
BuildRequires:  python3-zombie-imp
Requires:       python3-zombie-imp
%endif

%description
This application corrects your previous console command.
If you use BASH, you should add these lines to your .bashrc:
alias fuck='eval $(thefuck $(fc -ln -1)); history -r'
alias FUCK='fuck'
For other shells please check /usr/share/doc/thefuck/README.md

%prep
%autosetup
%py3_shebang_fix *.py

# Fix deprecated python3-mock https://github.com/nvbn/thefuck/issues/1262
find tests -type f -name '*.py' -exec sed -i -E 's/^(\s*)import mock/\1from unittest import mock/' {} \;
find tests -type f -name '*.py' -exec sed -i -E 's/^(\s*)from mock import /\1from unittest.mock import /' {} \;

# Cleanup requirements for release and functional tests
grep -Ev '^(flake8|mock|pexpect|pypandoc|pytest-benchmark|pytest-docker-pexpect|twine)\s*$' requirements.txt | tee requirements-filtered.txt

# Don't generate (unfiltered) dependencies for tox:
sed -Ei 's/[-]rrequirements\.txt//' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t requirements-filtered.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files thefuck

%check
%tox

%files -n thefuck -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/fuck
%{_bindir}/thefuck

%changelog
%autochangelog
