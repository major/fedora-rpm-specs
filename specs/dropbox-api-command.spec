#global commit 446e6e382f7e79744549f72436cd5407cefac8db
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dropbox-api-command
Version:        2.13
Release:        17%{?dist}
Summary:        Dropbox API wrapper command

License:        MIT
URL:            https://github.com/s-aska/%{name}
Source0:        https://github.com/s-aska/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
A command line tool to manage a directory synced with Dropbox.


%prep
%setup -q -n %{name}-%{version}


%build
%{__perl} Build.PL --installdirs=vendor
./Build


%install
./Build install --destdir=%{buildroot} --create_packlist=0

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README.md
%license LICENSE
%{_bindir}/dropbox-api
%{_bindir}/upload-to-dropbox
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 26 2023 Ben Boeckel <fedora@me.benboeckel.net> - 2.13-13
- Fix manpages in filelists (rhbz#2189098)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-9
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-6
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.13-3
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Ben Boeckel <mathstuf@gmail.com> - 2.13-1
- Update to 2.13

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-9
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-6
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.09-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Ben Boeckel <mathstuf@gmail.com> - 2.09-1
- update to 2.09

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.17-7
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Mar 02 2015 Ben Boeckel <mathstuf@gmail.com> - 1.17-5
- use proper Module::Build arguments

* Fri Feb 27 2015 Ben Boeckel <mathstuf@gmail.com> - 1.17-4
- update name for extraction

* Fri Feb 27 2015 Ben Boeckel <mathstuf@gmail.com> - 1.17-3
- use the tag for the Source
- change URL to GitHub
- add BuildRequires
- address review comments

* Thu Feb 26 2015 Ben Boeckel <mathstuf@gmail.com> - 1.17-2
- drop directory ownership

* Tue Feb 24 2015 Ben Boeckel <mathstuf@gmail.com> - 1.17-1
- initial package
