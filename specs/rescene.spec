# No debugging info because the built .exe is bytecode. Re-enable
# if we get AOT working.
%global debug_package %{nil}

Name:           rescene
Version:        1.2
Release:        32%{?dist}
Summary:        Extracts RAR metadata and recreates RAR files
License:        MIT
# Upstream at http://rescene.info/ appears to have gone away. Mirror is
# maintained at:
URL:            http://rescene.wikidot.com/
Source0:        http://rescene.wdfiles.com/local--files/downloads/srr.%{version}.cs.zip

BuildRequires:  mono-core
Requires:       mono-core
ExclusiveArch:  %{mono_arches}

%description
ReScene is a mechanism for backing up and restoring the metadata from
RAR archives.


%prep
%setup -q -c
cat >rescene.shell_script <<EOS
#!/bin/sh

mono "%{_libdir}/%{name}/srr.exe" "\$@"
EOS

# Fix EOL encodings
sed -i -e "s|\r||" license.txt



%build
mcs -unsafe -out:srr.exe *.cs

# Enabling AOT compilation causes rpmbuild to fail generating debuginfo.
# Disable it for now.
#mono --aot -O=all rescene.exe


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}

install -m 755 srr.exe $RPM_BUILD_ROOT%{_libdir}/%{name}/
# Enabling AOT compilation causes rpmbuild to fail generating debuginfo.
# Disable it for now.
#install -m 755 rescene.exe.so $RPM_BUILD_ROOT%%{_libdir}/%%{name}/
install -m 755 rescene.shell_script $RPM_BUILD_ROOT%{_bindir}/srr



%files
%doc license.txt
%{_libdir}/%{name}
%{_bindir}/srr


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Conrad Meyer <cemeyer@uw.edu> - 1.2-11
- 'gmcs' is removed; replace with simply 'mcs' (rh #1224044)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Conrad Meyer <cemeyer@uw.edu> - 1.2-8
- Update upstream, Source0 URLs to point to wikidot mirror

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Dan Horák <dan[at]danny.cz> - 1.2-3
- updated the supported arch list

* Thu Aug 26 2010 Conrad Meyer <konrad@tylerc.org> - 1.2-2
- Change to upstream binary name, "srr".
- Escape commented RPM macros so we don't get surprise expansions.

* Tue Aug 24 2010 Conrad Meyer <konrad@tylerc.org> - 1.2-1
- Bump to 1.2.
- Added support for archives with Unicode (actually UTF-8) encoded file
  names.
- Fixed a bug that caused errors when reconstructing archives with extra
  data (or padding) in their File Blocks. Specifically, if an archive
  contains a file that has a packed size larger than its original size
  (something that shouldn't ever happen with m0 compression), older
  versions of ReScene would repeat the last valid buffer of data to fill
  the difference, resulting in CRC (and SFV) errors on the last
  reconstructed file. This build fills the difference with null bytes
  instead and does not include the extra data in the CRC calculation.
  Note that although this change seems to have fixed all known issues
  with such archives, since there's no reason for the situation to occur
  in the first place, there's no guarantee this fix will handle all such
  archives in future.

* Mon Apr 26 2010 Conrad Meyer <konrad@tylerc.org> - 1.1-1
- Bump version, changelog:
  - Added -r switch to enable support for auto-locating renamed files. When
    this switch is used, if a file needed for reconstruction cannot be located
    in the input directory, the program will look for another file with the
    same extension and file size and attempt to use it instead.
  - Added archived file list to the output when using the -l switch.
  - Fixed a bug that caused an error when reconstructing a release that had
    directory structure preserved in the RAR archive. Now no attempt is made to
    open directories or 0-byte files during reconstruction since no data would
    be needed from them anyway.

* Mon Dec 14 2009 Conrad Meyer <konrad@tylerc.org> - 1.0-3
- Update license (clarified with upstream, again).

* Thu Dec 3 2009 Conrad Meyer <konrad@tylerc.org> - 1.0-2
- Update license (clarified with upstream).

* Wed Dec 2 2009 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Initial package.
