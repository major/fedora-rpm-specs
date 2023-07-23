%global _description %{expand:
Python interface to Bluetooth LE on Linux.
This is a project to provide an API to allow
access to Bluetooth Low Energy devices from Python.}

%global forgeurl https://github.com/IanHarvey/bluepy
%global  commit      7ad565231a97c304c0eff45f2649cd005e69db09
%global  date        20210503
%global  shortcommit %(c=%{commit}; echo ${c:0:8})

Name:           python-bluepy
Version:        1.3.0^%{date}git%{shortcommit}
Release:        3%{dist}
Summary:        Python interface to Bluetooth LE

#bluepy uses code from the bluez project, which is made available under
#Version 2 of the GNU Public License, bluepy itself is placed in the
#public domain
License:        Public Domain and GPLv2
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/bluepy-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description %_description

%package -n python3-bluepy
Summary:        %{summary}
BuildRequires:  python3-devel make gcc
BuildRequires:  glib2-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}
%{?python_provide:%python_provide python3-bluepy}

%description -n python3-bluepy %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}.

%prep
%autosetup -n bluepy-%{commit}
rm -rf bluepy.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%set_build_flags
export PYTHONPATH=../
sed 's|CFLAGS =|CFLAGS +=|g' -i bluepy/Makefile
sed 's|CPPFLAGS =|CPPFLAGS +=|g' -i bluepy/Makefile
sed 's| $(LDLIBS)| $(LDFLAGS) $(LDLIBS)|g' -i bluepy/Makefile
%py3_build
make -C docs SPHINXBUILD=sphinx-build-3 html
rm -rf docs/_build/html/{.doctrees,.buildinfo,.nojekyll} -vf

%install
%py3_install
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitelib}/bluepy/{get_services,scanner}.py
for file in %{buildroot}%{_bindir}/{thingy52,sensortag,blescan}; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/bluepy/{get_services,scanner}.py; do
   chmod a+x $file
done
for file in %{buildroot}%{python3_sitelib}/bluepy/{*.c,*.h}; do
   rm -rf $file
done

%files -n python3-bluepy
%{python3_sitelib}/bluepy/
%{python3_sitelib}/bluepy-*.egg-info/
%{_bindir}/blescan
%{_bindir}/sensortag
%{_bindir}/thingy52
%license LICENSE.txt
%doc README README.md

%files doc
%license LICENSE.txt
%doc docs/_build/html

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0^20210503git7ad56523-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.3.0^20210503git7ad56523-2
- Rebuilt for Python 3.12

* Mon Jan 30 2023 Alessio <alciregi AT fedoraproject DOT org> - 1.3.0^20210503git7ad56523-1
- Update to 2021-05-03 git commit

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.3.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 9 2019 Alessio <alciregi AT fedoraproject DOT org> - 1.3.0-1
- Initial package
