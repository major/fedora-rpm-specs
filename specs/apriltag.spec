Name:           apriltag
Version:        3.4.2
Release:        3%{?dist}
Summary:        Visual fiducial system popular for robotics research

# The entire source code BSD-2-Clause-Views except common/pthreads_cross.{cpp,h} which is MIT
License:        BSD-2-Clause-Views AND MIT
URL:            https://april.eecs.umich.edu/software/apriltag
Source0:        https://github.com/AprilRobotics/apriltag/archive/v%{version}/%{name}-%{version}.tar.gz

# Merged upstream as https://github.com/AprilRobotics/apriltag/pull/360
Patch0:         %{name}-3.4.2-test-directory.patch
# Merged upstream as https://github.com/AprilRobotics/apriltag/pull/364
Patch1:         %{name}-3.4.2-cmake-config-directory.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
AprilTag is a visual fiducial system popular in robotics research. This package
contains the most recent version of AprilTag, AprilTag 3, which includes a
faster (>2x) detector, improved detection rate on small tags, flexible tag
layouts, and pose estimation. AprilTag consists of a small C library with
minimal dependencies.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description devel
Development files for the %{name} package.


%prep
%autosetup -p1


%build
%cmake \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_TESTING:BOOL=ON \
  -DBUILD_PYTHON_WRAPPER:BOOL=OFF \
  -DCMAKE_C_STANDARD:STRING=99 \
  %{nil}
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE.md
%doc README.md
%{_libdir}/lib%{name}.so.3*

%files devel
%{_includedir}/apriltag/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 20 2024 Scott K Logan <logans@cottsay.net> - 3.4.2-2
- Add upstream patch to install cmake config to libdir

* Wed Oct 09 2024 Scott K Logan <logans@cottsay.net> - 3.4.2-1
- Update to 3.4.2
- Drop cmake version suffix from macros
- Use ctest now that upstream added some tests

* Mon Jan 08 2024 Scott K Logan <logans@cottsay.net> - 3.3.0-3
- Add usptream patch to clarify license text
- Invoke demo (without inputs) during check

* Wed Aug 23 2023 Scott K Logan <logans@cottsay.net> - 3.3.0-2
- Update license declaration
- Use SONAME in library file wildcard
- Minimize demo-dropping patch

* Tue Jan 31 2023 Scott K Logan <logans@cottsay.net> - 3.3.0-1
- Initial package (rhbz#2173758)
