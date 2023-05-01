Name:           rakudo
Version:        2023.04
Release:        %autorelease
Summary:        Raku on MoarVM, JVM, and JS
License:        Artistic-2.0
URL:            https://rakudo.org/
Source0:        https://github.com/rakudo/rakudo/releases/download/%{version}/rakudo-%{version}.tar.gz
Source1:        macros.raku

BuildRequires:  gcc make perl
BuildRequires:  libatomic_ops-devel libuv-devel libtommath-devel libffi-devel mimalloc-devel

BuildRequires:  moarvm-devel >= %{version}
BuildRequires:  nqp >= %{version}

Requires:       moarvm >= %{version}
Requires:       nqp >= %{version}

%description
Rakudo is a Raku Programming Language compiler for the MoarVM, JVM
and Javascript virtual machines.

%prep
%autosetup

%build
perl Configure.pl --prefix=%{_prefix} --backends=moar
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_mandir}/man1
pod2man --center="Rakudo Manual" --release="Raku" --section=1 --name=%{name} \
    docs/running.pod | gzip -c > %{buildroot}%{_mandir}/man1/%{name}.1.gz
ln -s rakudo.1.gz %{buildroot}%{_mandir}/man1/raku.1.gz

install -pDm755 tools/install-dist.raku %{buildroot}%{_bindir}/raku-install-dist

# Raku RPM macros
install -d %{buildroot}%{_rpmconfigdir}/macros.d
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
rm t/09-moar/01-profilers.t
%endif
make test

%files
%doc README.md
%license LICENSE
%{_bindir}/perl6*
%{_bindir}/raku
%{_bindir}/raku-debug
%{_bindir}/%{name}*
%{_bindir}/raku-install-dist

%{_datadir}/perl6/core
%{_datadir}/perl6/lib
%{_datadir}/perl6/runtime
%{_datadir}/perl6/site
%{_datadir}/perl6/vendor

%{_mandir}/man1/raku.1.gz
%{_mandir}/man1/%{name}.1.gz
%{_rpmconfigdir}/macros.d/macros.raku

%changelog
%autochangelog
