Name:           python-black
Version:        23.7.0
Release:        1%{?dist}
Summary:        The uncompromising code formatter
License:        MIT
URL:            https://github.com/psf/black
Source:         %{pypi_source black}

BuildArch:      noarch

BuildRequires:  python3-devel

# test requirements (upstream mixed with coverage, we hand-pick what we need only):
BuildRequires:  python3-pytest

# the black[jupyter] extra is allowed by default
# disable to avoid the ipython-black bootstrap loop
# note that tests/test_no_ipynb.py only runs without jupyter
# extra paranoid packagers can build this both with and without to run all tests
%bcond jupyter  1

# uvloop not ready for Python 3.12: https://bugzilla.redhat.com/2203920
%bcond uvloop   %[ 0%{?fedora} < 39 && 0%{?rhel} < 10 ]


%global _description %{expand:
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.}

%description %_description


%package -n     black
Summary:        %{summary}
Recommends:     black+d = %{version}-%{release}
%py_provides    python3-black

# The [python2] extra was removed in 22.1.0
# This can be safely removed in Fedora 39+
Obsoletes:      black+python2 < 22.1.0

%if %{without uvloop}
# The [uvloop] extra was temporarily removed in 23.7.0
# This can be safely removed once it is back or in Fedora 41+
Obsoletes:      black+uvloop < 23.7.0
%endif

%description -n black %_description


%prep
%autosetup -n black-%{version} -p1


%generate_buildrequires
%global extras_without_d colorama%{?with_jupyter:,jupyter}%{?with_uvloop:,uvloop}
%pyproject_buildrequires -rx d,%{extras_without_d}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'black*' '_black*' blib2to3

for exe in black blackd; do
  ln -sr %{buildroot}%{_bindir}/${exe}{,-%{python3_version}}
done


%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
%pytest -Wdefault -rs --run-optional %{!?with_jupyter:no_}jupyter


%files -n black -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/black
%{_bindir}/black-%{python3_version}

%pyproject_extras_subpkg -n black d
%{_bindir}/blackd
%{_bindir}/blackd-%{python3_version}

%pyproject_extras_subpkg -n black %{extras_without_d}


%changelog
* Thu Jul 13 2023 Miro Hrončok <mhroncok@redhat.com> - 23.7.0-1
- Update to 23.7.0
- Fixes: rhbz#2132839

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Miro Hrončok <mhroncok@redhat.com> - 22.8.0-1
- Update to 22.8.0
- Package the black[jupyter] extra
- Fixes: rhbz#2101619

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 22.3.0-2
- Rebuilt for Python 3.11

* Wed Apr 06 2022 Charalampos Stratakis <cstratak@redhat.com> - 22.3.0-1
- Update to 22.3.0
- Fixes: rhbz#2069385

* Wed Feb 02 2022 Miro Hrončok <mhroncok@redhat.com> - 22.1.0-1
- Update to 22.1.0
- Fixes rhbz#2029241

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.11~b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Miro Hrončok <mhroncok@redhat.com> - 21.11~b0-1
- Update to 21.11b0
- Fixes rhbz#1983119

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.6~b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Miro Hrončok <mhroncok@redhat.com> - 21.6~b0-1
- Update to 21.6b0
- Fixes rhbz#1957006

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 21.4~b2-3
- Rebuilt for Python 3.10

* Wed Apr 28 2021 Miro Hrončok <mhroncok@redhat.com> - 21.4~b2-2
- Update to 21.4b2
- Install primer.json with black
- Drop outdated downstream-only manual pages
- Package "d" and "python2" extras separately
- Fixes rhbz#1954694

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.8~b1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.8~b1-1
- Update to 20.8b1
- Fixes rhbz#1872790

* Wed Aug 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.8~b0-1
- Update to 20.8b0
- Fixes rhbz#1872743

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10~b0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 03 2020 Adam Williamson <awilliam@redhat.com> - 19.10~b0-3
- Rebuilt for Python 3.9
- Fix one test and hack up another one for Python 3.9 parser issues

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.10~b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Miro Hrončok <mhroncok@redhat.com> - 19.10~b0-1
- Update to 19.10b0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.3b0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-2
- Rename the binary package to black, rhbz#1692117

* Thu Mar 21 2019 Christian Heimes <cheimes@redhat.com> - 19.3b0-1
- New upstream release 19.3b0, rhbz#1688957

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.9b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Christian Heimes <cheimes@redhat.com> - 18.9b0-1
- New upstream version 18.9b0
- Include blackd daemon

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6b4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b4-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Christian Heimes <cheimes@redhat.com> - 18.6b4-1
- New upstream release 18.6b4, rhbz#1593485
- Remove workaround for missing empty_pyproject.toml

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b2-3
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-2
- Add new build and runtime dependency python3-toml
- Don't download external packages in tests
- Create missing empty_pyproject.toml for tests

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-1
- New upstream release 18.6b2, rhbz#1589399

* Wed Jun 06 2018 Christian Heimes <cheimes@redhat.com> - 18.6b1-1
- New upstream release 18.6b1

* Tue May 29 2018 Christian Heimes <cheimes@redhat.com> - 18.5b1-1
- New upstream release 18.5b0, rhbz#1579822

* Fri May 04 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-2
- Add man page
- Ignore false spelling warnings

* Wed May 02 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-1
- Initial package.
