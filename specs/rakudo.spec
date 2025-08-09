Name:           rakudo
Version:        2025.06
Release:        %autorelease
Summary:        Raku on MoarVM, JVM, and JS
License:        Artistic-2.0
URL:            https://rakudo.org/
Source0:        https://github.com/rakudo/rakudo/releases/download/%{version}/rakudo-%{version}.tar.gz
Source1:        macros.raku

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  libatomic_ops-devel
BuildRequires:  libuv-devel
BuildRequires:  libtommath-devel
BuildRequires:  libffi-devel
BuildRequires:  mimalloc-devel

BuildRequires:  moarvm-devel >= %{version}
BuildRequires:  nqp >= %{version}

Requires:       moarvm >= %{version}
Requires:       nqp >= %{version}

%description
Rakudo is a Raku Programming Language compiler for the MoarVM, JVM and
Javascript virtual machines.

%prep
%autosetup -p1

%build
perl Configure.pl --prefix=%{_prefix} --backends=moar
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
pod2man --center="Rakudo Manual" --release="Raku" --section=1 --name=rakudo \
    docs/running.pod | gzip -c > %{buildroot}%{_mandir}/man1/rakudo.1.gz
ln -s rakudo.1.gz %{buildroot}%{_mandir}/man1/raku.1.gz

install -pDm755 tools/install-dist.raku %{buildroot}%{_bindir}/raku-install-dist

# Raku RPM macros
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -pDm0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.raku

# Avoid duplicates by creating symbolic links.
for i in %{buildroot}%{_bindir}/perl6* %{buildroot}%{_datadir}/perl6/runtime/perl6*; do
    dir=$(dirname $i)
    f=$(basename $i | sed 's/perl6/rakudo/')
    if [ -e $dir/$f ]; then
        ln -sf $f $i
    fi
done

# remove zero-length files
rm -r %{buildroot}%{_datadir}/perl6/core/precomp/
rm %{buildroot}%{_datadir}/perl6/core/repo.lock

%check
%ifarch i686
rm t/06-telemetry/01-basic.t
%endif
make test

%files
%license LICENSE
%doc README.md
%{_bindir}/perl6*
%{_bindir}/raku
%{_bindir}/raku-debug
%{_bindir}/rakudo*
%{_bindir}/raku-install-dist
%{_datadir}/perl6/
%{_mandir}/man1/raku.1*
%{_mandir}/man1/rakudo.1*
%{_rpmconfigdir}/macros.d/macros.raku

%changelog
%autochangelog
