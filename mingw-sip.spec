%global pypi_name sip


Name:           mingw-%{pypi_name}
Summary:        MinGW Windows SIP6
Version:        6.6.2
Release:        5%{?dist}

# sipgen/parser.{c.h} is GPLv3+ with exceptions (bison)
License:        (GPLv2 or GPLv3) and (GPLv3+ with exceptions)
Url:            http://www.riverbankcomputing.com/software/sip/intro
Source0:        %{pypi_source}

# Backport fix for the instantiation of template values
Patch0:         323d39a2d602.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-setuptools

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-setuptools


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


%build
# Host build
%{mingw32_py3_build_host}
%{mingw64_py3_build_host}

# Target build
%{mingw32_py3_build}
%{mingw64_py3_build}


%install
# Host build
%{mingw32_py3_install_host}
%{mingw64_py3_install_host}

# Target build
%{mingw32_py3_install}
%{mingw64_py3_install}

# Fix extension
mv %{buildroot}%{mingw32_python3_sitearch}/sipbuild/code_generator.abi3.so %{buildroot}%{mingw32_python3_sitearch}/sipbuild/code_generator.abi3.pyd
mv %{buildroot}%{mingw64_python3_sitearch}/sipbuild/code_generator.abi3.so %{buildroot}%{mingw64_python3_sitearch}/sipbuild/code_generator.abi3.pyd


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
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/mingw32-sip-*
%{_prefix}/%{mingw32_target}/bin/sip-*
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/sipbuild/
%{_prefix}/%{mingw32_target}/lib/python%{mingw32_python3_version}/site-packages/sip-%{version}*-py%{mingw32_python3_version}.egg-info/
%{mingw32_bindir}/sip-*
%{mingw32_python3_sitearch}/sipbuild/
%{mingw32_python3_sitearch}/sip-%{version}*-py%{mingw32_python3_version}.egg-info/

%files -n mingw64-%{pypi_name}
%license LICENSE LICENSE-GPL2 LICENSE-GPL3
%{_bindir}/mingw64-sip-*
%{_prefix}/%{mingw64_target}/bin/sip-*
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/sipbuild/
%{_prefix}/%{mingw64_target}/lib/python%{mingw64_python3_version}/site-packages/sip-%{version}*-py%{mingw64_python3_version}.egg-info/
%{mingw64_bindir}/sip-*
%{mingw64_python3_sitearch}/sipbuild/
%{mingw64_python3_sitearch}/sip-%{version}*-py%{mingw64_python3_version}.egg-info/


%changelog
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
