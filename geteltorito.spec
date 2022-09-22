Name:           geteltorito
Version:        0.6
Release:        16%{?dist}
Summary:        El Torito boot image extractor

License:        GPLv2+
URL:            https://userpages.uni-koblenz.de/~krienke/ftp/noarch/%{name}
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  perl-generators

BuildArch:      noarch

%description
call:   geteltorito CD-image > toritoimagefile
example:geteltorito /dev/sr0  > /tmp/bootimage

The perl-script will extract the initial/default boot image from a CD if
existent.  It will not extract any of other possibly existing bootimages
that are allowed by the El Torito standard.
The imagedata are written to STDOUT, all other information is written to
STDERR (eg type and size of image).
If you want to write the image to a file instead of STDOUT you can
specify the filename wanted on the commandline using option -o <filename>.


%prep
%autosetup -cp 1


%install
%{__install} -Dpm 0755 %{name}/%{name}.pl %{buildroot}%{_bindir}/%{name}


%files
%doc %{name}/README
%license %{name}/gpl.txt
%{_bindir}/%{name}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 05 2018 Björn Esser <besser82@fedoraproject.org> - 0.6-7
- Use release tarball from upstream

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6-3
- Add few BRs
- Trivial fixes

* Tue Jun 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.6-2
- Fix spelling
- Trivial fixes

* Sun Jan 31 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.6-1
- Initial package
