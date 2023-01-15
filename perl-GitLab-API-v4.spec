%global src_name GitLab-API-v4


Name:           perl-%{src_name}
Version:        0.26
Release:        6%{?dist}
Summary:        Complete GitLab API v4 client

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/%{src_name}

# Doesn't work.  :(
# Source0:      https://www.cpan.org/modules/by-module/GitLab/%%{src_name}-%%{version}.tar.gz
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/%{src_name}-%{version}.tar.gz

# Fixed incorrect license messaging in POD backported from upstream
Patch0:         GitLab-API-v4-0.26-Update-license-POD.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.010
BuildRequires:  perl(Carp)
BuildRequires:  perl(Const::Fast) >= 0.014
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Tiny) >= 0.059
BuildRequires:  perl(HTTP::Tiny::Multipart) >= 0.05
BuildRequires:  perl(IO::Prompter) >= 0.004014
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(JSON) >= 2.59
BuildRequires:  perl(Log::Any) >= 1.703
BuildRequires:  perl(Log::Any::Adapter) >= 1.703
BuildRequires:  perl(Log::Any::Adapter::Screen) >= 0.13
BuildRequires:  perl(MIME::Base64) >= 3.15
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moo) >= 2.003000
BuildRequires:  perl(Path::Tiny) >= 0.079
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Test2::V0) >= 0.000094
BuildRequires:  perl(Try::Tiny) >= 0.28
BuildRequires:  perl(Types::Common::Numeric) >= 1.002001
BuildRequires:  perl(Types::Common::String) >= 1.002001
BuildRequires:  perl(Types::Standard) >= 1.002001
BuildRequires:  perl(URI) >= 1.62
BuildRequires:  perl(URI::Escape) >= 1.72
BuildRequires:  perl(namespace::clean) >= 0.27
BuildRequires:  perl(strict)
BuildRequires:  perl(strictures) >= 2.000003


%description
This module provides a one-to-one interface with the GitLab API v4.
Much is not documented here as it would just be duplicating GitLab's
own API Documentation.


%prep
%autosetup -n %{src_name}-%{version} -p 1


%build
perl Build.PL --installdirs=vendor
./Build


%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man*/*


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-5
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-2
- Perl 5.34 rebuild

* Tue May 11 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.26-1
- 0.26 bump
- License changed from 'GPLv3+' to 'GPL+ or Artistic'

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.25-2
- Perl 5.32 rebuild

* Thu Feb 13 2020 Björn Esser <besser82@fedoraproject.org> - 0.25-1
- New upstream release (#1802340)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-1
- New upstream release (#1763344)

* Wed Oct 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.22-1
- New upstream release (#1752080)

* Thu Aug 29 2019 Björn Esser <besser82@fedoraproject.org> - 0.21-1
- New upstream release (#1747004)

* Wed Jul 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.20-1
- New upstream release (#1732684)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.30 rebuild

* Sat May 18 2019 Björn Esser <besser82@fedoraproject.org> - 0.19-2
- License changed to GPLv3+

* Sat May 18 2019 Björn Esser <besser82@fedoraproject.org> - 0.19-1
- New upstream release (#1711471)

* Thu Apr 04 2019 Björn Esser <besser82@fedoraproject.org> - 0.18-1
- New upstream release (#1696124)

* Mon Feb 25 2019 Björn Esser <besser82@fedoraproject.org> - 0.17-1
- Bump release to stable (#1680372)

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.17-0.3
- Changes as suggested in review (#1680372)
- Add a set of explicit BuildRequires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.17-0.2
- Add explicit perl module compat requires

* Sun Feb 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.17-0.1
- Initial rpm release (#1680372)
