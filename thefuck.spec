Name: thefuck
Version: 3.32
Release: 4%{?dist}
Summary: App that corrects your previous console command
License: MIT
URL: https://github.com/nvbn/thefuck
Source0: https://github.com/nvbn/%{name}/archive/%{version}.tar.gz

BuildRequires: python3-devel
BuildArch: noarch

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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.32-3
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 10 2022 Arthur Bols <arthur@bols.dev> - 3.32-1
- Upstream release 3.32
- Updated spec to comply with updated guidelines

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.15-14
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.15-11
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.15-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.15-8
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.15-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Matias Kreder <delete@fedoraproject.org> 3.15-1
- Updated to thefuck 3.15

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-3
- Added buildrequires

* Wed Nov 18 2015 Matias Kreder <delete@fedoraproject.org> 3.2-1
- Updated to thefuck 3.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul 2 2015 Matias Kreder <delete@fedoraproject.org> 1.46-1
- Initial spec
