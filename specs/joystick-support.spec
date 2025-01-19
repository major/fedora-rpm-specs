Name: joystick-support          
Version:        1.0.0
Release:        35%{?dist}
Summary:        Load joystick / game pad drivers at boot time


License:        MIT
# The package is built just using this specfile.
#URL:            
#Source0:        

Requires:       kmod(joydev.ko)
Requires:       kmod(analog.ko)
Requires:       systemd

BuildArch:      noarch

%description
By default the joystick and game pad drivers are not loaded at boot time. Nor
are they installed by default. Installing this package will load the main
joystick and game pad drivers as part of the install, will bring in
kernel-modules-extra if it is needed (which it currently is), and will set 
things so that they will be loaded during future boots.


%prep

%build

%install
# Note that the modules-load.d man page states that packages should install
# files in /usr/lib/modules-load.d and that /etc/modules-load.d is
# reserved for local administration.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo -e "joydev\nanalog" > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/joystick.conf


%files
%{_libdir}/../lib/modules-load.d/joystick.conf

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Mar 20 2024 Tim Landscheidt <tim@tim-landscheidt.de> - 1.0.0-33
- Remove obsolete requirements for post scriptlet

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Dennis Gilmore <dennis@ausil.us> - 1.0.0-16
- remove the %%post scipts during new installs we can not modprobe which causes anaconda to fail

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.0-13
- kernel-modules-extra was never dropped on ARM
- It's possible to use tradional game controllers on ARM via GPIO mods

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bruno Wolff III <bruno@wolff.to> 1.0.0-11
- Use new kernel module provides to get kernel-modules-extra

* Mon Jan 20 2014 Bruno Wolff III <bruno@wolff.to> 1.0.0-10
- Require installonlypkg(kernel-module) instead on kernel-modules-extra

* Wed Oct 09 2013 Bruno Wolff III <bruno@wolff.to> 1.0.0-9
- Back to excluding arm arch instead of trying to drop requires

* Tue Oct 08 2013 Bruno Wolff III <bruno@wolff.to> 1.0.0-8
- Use a macro for arm arches, plain arm doesn't work as expected

* Tue Oct 08 2013 Bruno Wolff III <bruno@wolff.to> 1.0.0-7
- Don't require kernel-modules-extra on arm

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-4
- Bump release since a -3 sprm was published in the review bug

* Tue Aug 28 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-3
- Do another build without the macro in changelog problem

* Tue Aug 28 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-2
- Require systemd for modules-load.d directory.
- Use empty %%build since %%build can do stuff on its own.
- Remove deprecated buildroot clean.

* Mon Jul 23 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-1
- Initial package creation
