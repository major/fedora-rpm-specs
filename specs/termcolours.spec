Name:           termcolours
Version:        0.7.0
Release:        %autorelease
Summary:        Automatically set unique terminal colour schemes

License:        GPL-3.0-or-later
URL:            https://www.mavit.org.uk/termcolours/
Source:         https://codeberg.org/mavit/%{name}/releases/download/%{version}/App-%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Recommends:     (xrdb if xterm)

%{?perl_default_filter}


%description
Give a terminal a persistent unique background colour, generated from
the hostname (or some other string of your choosing).


%prep
%autosetup -n App-%{name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license LICENSE
%{_bindir}/termcolours
%{_mandir}/man1/*.1*


%changelog
%autochangelog
