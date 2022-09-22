%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}
%{!?lua_pkgdir: %global lua_pkgdir %{_datadir}/lua/%{lua_version}}


Name:        vicious
Version:     2.4.1
Release:     8%{?dist}
Summary:     Modular widget library for awesome

License:     GPLv2+
URL:         https://github.com/%{name}-widgets/%{name}
Source0:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:   noarch

Provides:    lua-%{name} = %{version}-%{release}

%if 0%{?fedora} || 0%{?rhel} >= 7
Requires:    lua(abi) = %{lua_version}
%else
Requires:    lua >= %{lua_version}
Requires:    lua <  %{lua: os.setlocale('C'); print(string.sub(_VERSION, 5) + 0.1)}
%endif

Recommends:  alsa-utils
Recommends:  curl
Recommends:  hddtemp
Recommends:  wireless-tools
Recommends:  iw

# This package is handy for the awesome window manager.
Suggests:    awesome

%description
Vicious widget types are a framework for creating your own awesome widgets.
Vicious contains modules that gather data about your system, and a few helper
functions that make it easier to register timers, suspend widgets and so on.


%prep
%autosetup -p 1


%build
for dir in contrib templates; do
  mv ${dir}/README.md README-${dir}.md
done


%install
mkdir -p %{buildroot}%{lua_pkgdir}/%{name}
cp -a */ *.lua %{buildroot}%{lua_pkgdir}/%{name}


%files
%doc Changes.md README* TODO
%license LICENSE
%{lua_pkgdir}/%{name}


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-3
- Rebuilt for Lua 5.4

* Mon Jun 29 2020 Björn Esser <besser82@fedoraproject.org> - 2.4.1-2
- Rebuild (lua)

* Mon May 25 2020 Björn Esser <besser82@fedoraproject.org> - 2.4.1-1
- New upstream release (#1766407)
- Move library to %%lua_pkgdir so can be used with any window manager
- Do not use macros for common commands
- Add Provides for lua-%%{name}
- Move README.md from templates dir into top-level dir

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.3-2
- Turn most hard requirements into weak dependencies (#1693384)
- Add Recommends: iw for use with an optional module

* Tue Mar 12 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.3-1
- New upstream release (#1687655)

* Fri Feb 15 2019 Björn Esser <besser82@fedoraproject.org> - 2.3.2-1
- New upstream release (#1490024)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 11 2014 Simon Erat <erat.simon@gmail.com> - 2.1.3-1
- new upstream release (#1048834)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 12 2013 Simon Erat <erat.simon@gmail.com> - 2.1.1-4
- Changed:   Summarytext

* Tue Sep 03 2013 Simon Erat <sea@fedorapeople.org> - 2.1.1-3
- general cleanup, reordered/grouped tags
- added needed Requires, %%build, more files to %%doc
- improved %%install

* Mon Sep 02 2013 Simon Erat <sea@fedorapeople.org> - 2.1.1-2
- Got it working with original upstream and changed %%summary

* Mon Sep 02 2013 Simon Erat <sea@fedorapeople.org> - 2.1.1-1
- Updated %%summary and %%description

* Mon Sep 02 2013 Simon Erat <sea@fedorapeople.org> - 2.1.1-0
- Initial rpm release
