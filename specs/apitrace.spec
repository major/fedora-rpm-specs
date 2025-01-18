#global commit c54d99563414cd178abec7cf7d9663eb949a0f51
#global shortcommit %(c=%{commit}; echo ${c:0:7})

# Update to submodule revision as in https://github.com/apitrace/apitrace/tree/master/thirdparty when updating
%global libbacktrace_commit 8602fda64e78f1f46563220f2ee9f7e70819c51d
%global libbacktrace_shortcommit %(c=%{libbacktrace_commit}; echo ${c:0:7})

Name:           apitrace
Version:        12.0
Release:        3%{?commit:.git%{shortcommit}}%{?dist}
Summary:        Tools for tracing OpenGL

License:        MIT
URL:            http://apitrace.github.io/
%if 0%{?commit:1}
# git clone --recursive https://github.com/apitrace/apitrace.git
# cd apitrace
# git archive --prefix=apitrace-$commit/ -o ../apitrace-${commit:0:7}.tar $commit
# git submodule foreach --recursive "git archive --prefix=apitrace-$commit/\$path/ --output=\$sha1.tar HEAD && tar --concatenate --file=$(pwd)/../apitrace-${commit:0:7}.tar \$sha1.tar && rm \$sha1.tar"
# cd ..
# gzip apitrace-${commit:0:7}.tar
Source0:        apitrace-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/apitrace/apitrace/archive/%{version}/apitrace-%{version}.tar.gz
%endif
Source1:        https://github.com/ianlancetaylor/libbacktrace/archive/%{libbacktrace_commit}/libbacktrace-%{libbacktrace_shortcommit}.tar.gz
Source2:        qapitrace.desktop
Source3:        qapitrace.appdata.xml

# Don't require third-party submodules
Patch0:         apitrace_nosubmodules.patch

BuildRequires:  brotli-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdwarf-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  snappy-devel

Requires:       %{name}-libs%{_isa} = %{version}-%{release}
# scripts/snapdiff.py
Requires:       python3-pillow

# See http://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:       bundled(md5-plumb)
# See https://fedorahosted.org/fpc/ticket/429
Provides:       bundled(libbacktrace)
# Modofied http://create.stephan-brumme.com/crc32/, see thirdparty/crc32c/README.md
Provides:       bundled(crc32c)


%description
apitrace consists of a set of tools to:
 * trace OpenGL and OpenGL ES  APIs calls to a file;
 * replay OpenGL and OpenGL ES calls from a file
 * inspect OpenGL state at any call while retracing
 * visualize and edit trace files


%package libs
Summary:        Libraries used by apitrace
Requires:       %{name} = %{version}-%{release}

%description libs
Libraries used by apitrace


%package gui
Summary:        Graphical frontend for apitrace
Requires:       %{name}%{_isa} = %{version}-%{release}

%description gui
This package contains qapitrace, the Graphical frontend for apitrace.


%prep
%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit} -a1
%else
%autosetup -p1 -n %{name}-%{version} -a1
%endif

# Remove bundled libraries, except khronos headers
rm -rf `ls -1d thirdparty/* | grep -Ev "(khronos|md5|crc32c|libbacktrace.cmake|support|CMakeLists.txt)"`

# Add bundled libbacktrace
mv libbacktrace-%{libbacktrace_commit} thirdparty/libbacktrace


%build
%cmake -DENABLE_STATIC_SNAPPY=OFF
%cmake_build


%install
%cmake_install

# Install doc through %%doc
rm -rf %{buildroot}%{_docdir}/

# Install desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE2}

# Install appdata file
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml
%{_bindir}/appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/qapitrace.appdata.xml

# highlight.py is not a script
chmod 0644 %{buildroot}%{_libdir}/%{name}/scripts/highlight.py


%check
# If run through ctest, libbacktrace_btest will fail with
#     ERROR: descriptor 3 still open after tests complete
# This is due to https://gitlab.kitware.com/cmake/cmake/-/issues/18863
# So, run the test outside of ctest
pushd %{_vpath_builddir}
ctest --output-on-failure -E libbacktrace_btest
./btest
popd


%files
%license LICENSE
%doc README.markdown docs/*
%{_bindir}/apitrace
%{_bindir}/eglretrace
%{_bindir}/glretrace
%{_bindir}/gltrim

%files libs
%{_libdir}/%{name}/

%files gui
%{_bindir}/qapitrace
%{_datadir}/applications/qapitrace.desktop
%{_datadir}/appdata/qapitrace.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Sandro Mani <manisandro@gmail.com> - 12.0-1
- Update to 12.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 24 2022 Sandro Mani <manisandro@gmail.com> - 11.1-1
- Update to 11.1

* Mon May 02 2022 Sandro Mani <manisandro@gmail.com> - 11.0-1
- Update to 11.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-6.gitd28a980
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Sandro Mani <manisandro@gmail.com> - 10.0-5.gitd28a980
- Update to git d28a980

* Wed Sep 01 2021 Sandro Mani <manisandro@gmail.com> - 10.0-4.git9d42f66
- Workaround glibc 2.34 build failure by disabling dlsym wrapper

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3.git9d42f66
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 09 2021 Jeff Law <jlaw@tachyum.com> - 10.0-2.git9d42f66
- Re-enable LTO

* Sat Apr 10 2021 Sandro Mani <manisandro@gmail.com> - 10.0-1.git9d42f66
- Update to 10.0

* Tue Feb 09 2021 Sandro Mani <manisandro@gmail.com> - 9.0-0.13.git590f2bb
- Update to git 590f2bb

* Wed Jan 27 2021 Sandro Mani <manisandro@gmail.com> - 9.0-0.12.git37c36e6
- Update to git 37c36e6

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-0.11.git1aa8391
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 18 2020 Sandro Mani <manisandro@gmail.com> - 9.0-0.10.git1aa8391
- Update to git 1aa8391

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-0.9.git433f99b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 9.0.0-0.8.git433f99b
- Disable LTO

* Wed Jan 29 2020 Sandro Mani <manisandro@gmail.com> - 9.0.0-0.7.git433f99b
- Update to git 433f99b

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-0.6.git0f541f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Sandro Mani <manisandro@gmail.com> - 0.9-0.5.git0f541f4
- Actually add patch to fix build with GCC10

* Tue Oct 22 2019 Sandro Mani <manisandro@gmail.com> - 9.0-0.4.git0f541f4
- Add patch to fix build with GCC10

* Tue Aug 06 2019 Sandro Mani <manisandro@gmail.com> - 9.0-0.3.git0f541f4
- Drop BR: python2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.0-0.2.git0f541f4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 9.0.0-0.1.git0f541f4
- Update to latest git
- Switch to python3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-0.2.gitf411d55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Sandro Mani <manisandro@gmail.com> - 0.8-0.1.gitf411d55
- Update to latest git

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 7.1-11
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Sandro Mani <manisandro@gmail.com> - 7.1-9
- Rebuild

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 7.1-8
- Correctly remove thirdparty bundled libraries (#1507659)
- Add BR: libdwarf-devel to enable backtrace support

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 7.1-7
- Don't add -nn to the moc options

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Sandro Mani <manisandro@gmail.com> - 7.1-1
- Update to 7.1

* Wed Sep 16 2015 Richard Hughes <rhughes@redhat.com> - 7.0-2
- Fix the AppData file to actually validate

* Thu Jul 23 2015 Sandro Mani <manisandro@gmail.com> - 7.0-1
- Update to 7.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 02 2015 Sandro Mani <manisandro@gmail.com> - 6.1-3
- Remove dlsym hack, use %%define __filter_GLIBC_PRIVATE 1

* Fri Jan 16 2015 Sandro Mani <manisandro@gmail.com> - 6.1-2
- Fix appdata file

* Fri Jan 16 2015 Sandro Mani <manisandro@gmail.com> - 6.1-1
- Update to 6.1

* Tue Jan 06 2015 Sandro Mani <manisandro@gmail.com> - 6.0-2
- Re-introduce dlsym hack

* Mon Jan 05 2015 Sandro Mani <manisandro@gmail.com> - 6.0-1
- Update to 6.0
- Ship appdata file

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Adam Jackson <ajax@redhat.com> 5.0-3
- Fix dlsym hack to work on arm (and probably others)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Sandro Mani <manisandro@gmail.com> - 5.0-1
- Update to 5.0

* Fri Mar 07 2014 Sandro Mani <manisandro@gmail.com> - 4.0-5
- Split off libs package
- Allow tracing 32bit binaries on 64bit

* Mon Nov 18 2013 Sandro Mani <manisandro@gmail.com> - 4.0-4
- chmod 0644 scripts/highlight.py
- Fix all python shebangs according to fedora guidelines
- Use BR: python2-devel
- Split off qapitrace into subpackage

* Sat Nov 16 2013 Sandro Mani <manisandro@gmail.com> - 4.0-3
- Fix desktop-file-install syntax

* Sat Nov 16 2013 Sandro Mani <manisandro@gmail.com> - 4.0-2
- Fix %%{_buildroot} -> %%{buildroot} typo
- Remove explicit BRs which are implicit

* Wed Nov 13 2013 Sandro Mani <manisandro@gmail.com> - 4.0-1
- Initial package
