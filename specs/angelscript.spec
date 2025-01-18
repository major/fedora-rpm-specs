%global optflags %(echo %{optflags} -fno-strict-aliasing)

%global _vpath_srcdir sdk/%{name}/projects/meson/

Name:           angelscript
Version:        2.35.1
Release:        7%{?dist}
Summary:        Flexible cross-platform scripting library

License:        zlib
URL:            http://www.angelcode.com/angelscript/
Source0:        %{url}/sdk/files/%{name}_%{version}.zip

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
The AngelScript library is a software library for easy integration of
external scripting to applications, with built-in compiler and virtual
machine. The scripting language is easily extendable to incorporate
application specific data types and functions. It is designed with C++
in mind, as such it shares many features with C++, for example syntax
and data types.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc sdk/docs/articles/*.html
%{_libdir}/lib%{name}.so.*

%files devel
%doc sdk/docs/manual/*
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Pete Walter <pwalter@fedoraproject.org> - 2.35.1-1
- Update to 2.35.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.32.0-4
- Add BuildRequires: gcc-c++

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenko@redhat.com> - 2.32.0-2
- Switch to %%ldconfig_scriptlets

* Sun Dec 31 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.32.0-1
- Update to 2.32.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 18 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.2-1
- Update to 2.31.2

* Fri Dec 16 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.1-4
- Use VPATH macro properly

* Fri Nov 25 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.1-3
- Build on all architectures

* Sun Nov 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.1-2
- Fix FTBFS (RHBZ #1385042)

* Mon Jun 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.1-1
- Update to 2.31.1 (RHBZ #1350286)

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.31.0-1
- Update to 2.31.0 (RHBZ #1312564)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.30.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.2-2
- Rebuild for new meson macros

* Tue Oct 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.2-1
- Update to 2.30.2

* Tue Jun 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-8
- Use -fno-strict-aliasing
- build only on primary arches

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-6
- Simplify buildsystem

* Thu May 21 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-5
- arm build fixes

* Wed May 20 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-4
- Fix arm building

* Mon May 18 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-3
- Fix docs in devel subpkg

* Wed May 13 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-2
- Use custom builsystem to avoid multiple patching Makefile

* Sun Apr 26 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.30.0-1
- Initial package
