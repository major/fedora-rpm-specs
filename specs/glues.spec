%undefine __cmake_in_source_build
%global commit0 44cb7c6eae4488f921041572908f3af508880547

Name:           glues
Version:        1.5
Release:        13.20200105git44cb7c6%{?dist}
Summary:        GLU port for OpenGL ES

# SGI FREE SOFTWARE LICENSE B (Version 2.0, Sept. 18, 2008)
License:        MIT
URL:            https://github.com/lunixbochs/%{name}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz

BuildRequires:  cmake gcc-c++
# TODO check compatibility for SDL 1.2+ currently in rawhide
BuildRequires:  SDL2-devel
BuildRequires:  mesa-libGL-devel


%description
This port is based on original GLU 1.3 and has original libutil, libtess and
nurbs libraries.


%package devel
Summary:        Development files for GLUES
Requires:       %{name}%{?_isa} = %{version}

%description devel
%summary.


%prep
%autosetup -n%{name}-%{commit0}
# rename so to avoid conflicts
sed -i 's,GLU ,GLUES ,' CMakeLists.txt
# skip nurbs
find source/libnurbs -type d -print -exec rm -rv '{}/*' \;


%build
%cmake
%cmake_build


%install
mkdir -p %{buildroot}%{_libdir}
install -p %{_vpath_builddir}/libGLUES.so* %{buildroot}%{_libdir}
ln -s libGLUES.so.* %{buildroot}%{_libdir}/libGLUES.so
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -pr source/*.h %{buildroot}%{_includedir}/%{name}

%files
%license LICENSE
%doc README docs/*
%{_libdir}/lib*.so.1

%files devel
%license LICENSE
%doc sdltests/
%{_libdir}/libGLUES.so
%{_includedir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3.20200105git44cb7c6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2.20200105git44cb7c6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jan 05 2020 Raphael Groner <projects.rg@smart.ms> - 1.5-1.20200105git44cb7c6
- initial


