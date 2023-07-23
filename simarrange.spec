%global commit 8238ce568c3ce23e1ad5fbfec55031907bd23f77
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global datestamp 20170316
%global relstring %{datestamp}git%{shortcommit}
Name:           simarrange
Version:        0.0
Release:        38%{relstring}%{?dist}
Summary:        STL 2D plate packer with collision simulation
License:        AGPLv3+
URL:            https://github.com/kliment/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:         simarrange-opencv4.patch
BuildRequires:  gcc-c++
BuildRequires:  admesh-devel
BuildRequires:  argtable-devel
BuildRequires:  opencv-devel
BuildRequires:  uthash-devel

%description
Simarrange is a program that simulates collisions between STL meshes in 2D in
order to generate tightly packed sets of parts. It takes a directory of STL
files as input and outputs STL files with combined plates of parts.
The parts are assumed to be in the correct printable orientation already.

%prep
%setup -qn %{name}-%{commit}
%patch0 -p1 -b .orig

# bundling
rm utlist.h

%build
# the build script is one line and would need patching, so just skip it
# TODO update to use Makefile
g++ %{optflags} simarrange.c -o ./%{name} -lm `pkg-config --cflags --libs opencv` \
    -ladmesh -largtable2 -fopenmp -DPARALLEL

%install
install -Dpm0755 ./%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 ./%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3820170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3720170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 0.0-3620170316git8238ce5
- Rebuild for opencv 4.7.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3520170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 0.0-3420170316git8238ce5
- Rebuilt for opencv 4.6.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3320170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 0.0-3220170316git8238ce5
- Rebuild(uthash)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3120170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-3020170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.0-2920170316git8238ce5
- Rebuilt for OpenCV

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-2820170316git8238ce5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-2720170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.0-2620170316git8238ce5
- Rebuilt for OpenCV 4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-2520170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.0-2420170316git8238ce5
- Rebuild for OpenCV 4.2

* Mon Jan 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.0-2320170316git8238ce5
- Update opencv4 patch

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.0-2220170316git8238ce5
- Rebuilt for opencv4

* Wed Sep 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0-21.20170316git8238ce5
- Rebuild for opencv (with vtk disabled)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-20.20170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-19.20170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-18.20170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 0.0-17.20170316git8238ce5
- Rebuild for opencv soname bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-16.20170316git8238ce5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Miro Hrončok <mhroncok@redhat.com> - 0.0-15.20170316git8238ce5
- Updated to the latest commit
- Rebuilt for new opencv

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-14.20170309git3300eb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-13.20170309git3300eb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Miro Hrončok <mhroncok@redhat.com> - 0.0-12.20150708git315be26
- Update to latest commit
- Rebuilt for new opencv
- Use the %%license tag
- README was renamed

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-11.20140729git9500190
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0-10.20140729git9500190
- Rebuilt for new opencv (#1230078)

* Thu May 05 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0-9.20140729git9500190
- Rebuilt for new opencv

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0-8.20140729git9500190
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Jozef Mlich <jmlich@redhat.com> - 0.0-7.20140729git9500190
- use pkg-config to determine opencv CFLAGS and LIBS instead of hardcoded values

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-6.20140729git9500190
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-5.20140729git9500190
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.0-4.20140729git9500190
- Fix date in release tag

* Tue Jul 29 2014 Miro Hrončok <mhroncok@redhat.com> - 0.0-3.20131019git9500190
- Update to new commit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0-2.20131019gitd52382f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Oct 22 2013 Miro Hrončok <mhroncok@redhat.com> - 0.0-1.20131019gitd52382f
- New package


