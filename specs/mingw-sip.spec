%global pypi_name sip


Name:           mingw-%{pypi_name}
Summary:        MinGW Windows SIP6
Version:        6.9.1
Release:        1%{?dist}

License:        BSD-2-Clause
Url:            http://www.riverbankcomputing.com/software/sip/intro
Source0:        %{pypi_source}
# Drop setuptools-scm requirement
Patch0:         sip_no-setuptools-scm.patch

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build


%description
MinGW Windows SIP6.


%package -n mingw32-%{pypi_name}
Summary:       MinGW Windows SIP6

%description -n mingw32-%{pypi_name}
MinGW Windows SIP6.


%package -n mingw64-%{pypi_name}
Summary:       MinGW Windows SIP6

%description -n mingw64-%{pypi_name}
MinGW Windows SIP6.


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Set version (see sip_no-setuptools-scm.patch)
sed -i 's|@version@|%version|' pyproject.toml


%build
# Host build
%{mingw32_py3_build_host_wheel}
%{mingw64_py3_build_host_wheel}

# Target build
%{mingw32_py3_build_wheel}
%{mingw64_py3_build_wheel}


%install
# Host build
%{mingw32_py3_install_host_wheel}
%{mingw64_py3_install_host_wheel}

# Target build
%{mingw32_py3_install_wheel}
%{mingw64_py3_install_wheel}


# Wrappers
mkdir -p %{buildroot}%{_bindir}

for file in %{buildroot}%{_prefix}/%{mingw32_target}/bin/sip-*; do
mv $file $file.py
cat << EOF > $file
#!/bin/sh
mingw32-python3 %{_prefix}/%{mingw32_target}/bin/`basename $file`.py "\$@"
EOF
chmod +x $file
ln -s %{_prefix}/%{mingw32_target}/bin/`basename $file` %{buildroot}%{_bindir}/mingw32-`basename $file`
done

for file in %{buildroot}%{_prefix}/%{mingw64_target}/bin/sip-*; do
mv $file $file.py
cat << EOF > $file
#!/bin/sh
mingw64-python3 %{_prefix}/%{mingw64_target}/bin/`basename $file`.py "\$@"
EOF
chmod +x $file
ln -s %{_prefix}/%{mingw64_target}/bin/`basename $file` %{buildroot}%{_bindir}/mingw64-`basename $file`
done


%files -n mingw32-%{pypi_name}
%license LICENSE
%{_bindir}/mingw32-sip-*
%{mingw32_bindir}/sip-*
%{mingw32_python3_sitearch}/sipbuild/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{_prefix}/%{mingw32_target}/bin/sip-*
%{mingw32_python3_hostsitearch}/sipbuild/
%{mingw32_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-%{pypi_name}
%license LICENSE
%{_bindir}/mingw64-sip-*
%{mingw64_bindir}/sip-*
%{mingw64_python3_sitearch}/sipbuild/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/
%{_prefix}/%{mingw64_target}/bin/sip-*
%{mingw64_python3_hostsitearch}/sipbuild/
%{mingw64_python3_hostsitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Dec 25 2024 Sandro Mani <manisandro@gmail.com> - 6.9.1-1
- Update to 6.9.1

* Sun Dec 08 2024 Sandro Mani <manisandro@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 6.8.6-1
- Update to 6.8.6

* Sat Feb 24 2024 Sandro Mani <manisandro@gmail.com> - 6.8.3-1
- Update to 6.8.3

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 6.8.2-1
- Update to 6.8.2

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 6.7.12-1
- Update to 6.7.12

* Sat Aug 12 2023 Sandro Mani <manisandro@gmail.com> - 6.7.11-1
- Update to 6.7.11

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 6.7.10-1
- Update to 6.7.10

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Sandro Mani <manisandro@gmail.com> - 6.7.9-1
- Update to 6.7.9

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 6.7.7-1
- Update to 6.7.7

* Thu Feb 02 2023 Sandro Mani <manisandro@gmail.com> - 6.7.6-1
- Update to 6.7.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 6.7.5-1
- Update to 6.7.5

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-6
- Switch to python3-build

* Tue Aug 09 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-5
- Backport fix for the instantiation of template values

* Wed Aug 03 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-4
- Proper host build

* Sat Jul 30 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-3
- Don't use expanded mingw-python macros in wrapper scripts

* Fri Jul 29 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-2
- Rebuild for mingw-filesystem-140

* Fri Jul 22 2022 Sandro Mani <manisandro@gmail.com> - 6.6.2-1
- Update to 6.6.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 6.5.1-1
- Update to 6.5.1

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 6.5.0-4
- Also build/install target build, drop manually specified requires

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 6.5.0-3
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Sandro Mani <manisandro@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 6.3.1-1
- Update to 6.3.1

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-2
- Require mingw-python-setuptools

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Sep 14 2021 Sandro Mani <manisandro@gmail.com> - 6.1.1-1
- Initial package
