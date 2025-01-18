Name: floppy-support          
Version:        1.0.0
Release:        31%{?dist}
Summary:        Load floppy driver at boot time


License:        MIT
# The package is built just using this specfile.
#URL:            
#Source0:        

Requires: kmod(floppy.ko)
Requires: systemd
Requires(post): module-init-tools

BuildArch:      noarch
# The floppy module does not appear to be built for arm (or the kernel 
# auto provides feature isn't turned on there.
ExcludeArch:    %{arm} aarch64 s390x

%description
By default the floppy driver is not loaded at boot time. Installing this
package will load the floppy driver as part of the install and will set
things so that it will be loaded during future boots. While the floppy
driver is currently in kernel-modules, it may move to kernel-modules-extra
in the future, and if so this package will bring that in.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
# Note that the modules-load.d man page states that packages should install
# files in /usr/lib/modules-load.d and that /etc/modules-load.d is
# reserved for local administration.
mkdir -p $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d
echo floppy > $RPM_BUILD_ROOT%{_libdir}/../lib/modules-load.d/floppy.conf


%files
%{_libdir}/../lib/modules-load.d/floppy.conf

%post
/sbin/modprobe floppy

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Dan Horák <dan[at]danny.cz> - 1.0.0-14
- kmod(floppy.ko) is also not available on s390x

* Wed Jun 28 2017 Till Maas <opensource@till.name> - 1.0.0-13
- kmod(floppy.ko) is also not available on aarch64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Bruno Wolff III <bruno@wolff.to> 1.0.0-8
- kmod(floppy.ko) is not available on arm

* Wed May 14 2014 Bruno Wolff III <bruno@wolff.to> 1.0.0-7
- Require the floppy kernel module in case it moves to kernel-modules-extra

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 28 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-4
- Do another build without the messed up changelog

* Tue Aug 28 2012 Bruno Wolff III <bruno@wolff.to> 1.0.0-3
- Fix up some things mentioned in the review.
- Require systemd to make sure the modules-load.d directory exists.
- Use %%build even though nothing is built as it can have side effects.

* Mon Sep 05 2011 Bruno Wolff III <bruno@wolff.to> 1.0.0-2
- Use %%{_libdir}/../lib/ instead of %%{_libdir} to avoid arch issues.

* Tue Aug 30 2011 Bruno Wolff III <bruno@wolff.to> 1.0.0-1
- Initial package creation
