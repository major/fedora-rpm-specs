%global srcname reedsolo

Name:           python-reedsolo
Version:        1.5.4
Release:        9%{?dist}
Summary:        Pure-Python Reed Solomon encoder/decoder
License:        Public Domain
URL:            https://github.com/tomerfiliba/reedsolomon
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A pure-python universal errors-and-erasures Reed-Solomon Codec, based on the
wonderful tutorial at wikiversity, written by “Bobmath” and “LRQ3000”.}

%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
%if 0%{?fedora} == 32
%py_provides python3-%{srcname}
%endif
%py_provides python3-c%{srcname}

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n reedsolomon-%{version}
rm -v creedsolo.c
# Remove shebang in non-script source
# https://github.com/tomerfiliba/reedsolomon/pull/31
sed -r -i '1{/^#!/d}' %{srcname}.py


%build
%py3_build


%install
%py3_install


%check
%pytest


%files -n  python3-%{srcname}
%license LICENSE
%doc changelog.txt README.rst
%pycached %{python3_sitearch}/%{srcname}.py
%{python3_sitearch}/c%{srcname}%{python3_ext_suffix}
%{python3_sitearch}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.4-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.4-5
- Rebuilt for Python 3.10

* Fri Mar 05 2021 Julian.Sikorski <belegdol@fedoraproject.org> - 1.5.4-4
- Do not hardcode x86_64

* Wed Mar 03 2021 Julian Sikorski <belegdol@fedoraproject.org> - 1.5.4-3
- Add changelog.txt to %%doc
- Add gcc to BuildRequires

* Wed Mar 03 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.5.4-2
- Implement review feedback

* Sat Feb 06 2021 Julian Sikorski <belegdol@fedoraproject.org> - 1.5.4-1
- Initial RPM release
