Name:           perl-MIME-Lite
Version:        3.038
Release:        %autorelease
Summary:        MIME::Lite - low-calorie MIME generator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Lite
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MIME-Lite-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::Date::Format) >= 1.000
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Recommends tests:
BuildRequires:  perl(MIME::Types) >= 1.28
# not detected by automated find-requires:
Requires:       perl(Email::Date::Format) >= 1.000
Recommends:     perl(MIME::Types) >= 1.28
Recommends:     perl(Mail::Address) >= 1.62

%{?perl_default_filter}

%description
MIME::Lite is intended as a simple, standalone module for generating (not
parsing!) MIME messages... Specifically, it allows you to output a simple,
decent single- or multi-part message with text or binary attachments.  It does
not require that you have the Mail:: or MIME:: modules installed.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n MIME-Lite-%{version}
sed -i 's/\r//' examples/*
sed -i 's/\r//' contrib/*
chmod a-x examples/* contrib/*
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cp -a testin %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes examples contrib
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/MIME::Lite.3pm.gz

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
