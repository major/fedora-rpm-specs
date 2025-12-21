# some tests are failing and there isn't a straightforward way to disable them
%bcond check 1
%global debug_package %{nil}

Name:           ruby-build
Version:        20251218
Release:        %autorelease
Summary:        Compile and install Ruby

License:        MIT
URL:            https://github.com/rbenv/ruby-build
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PR https://github.com/rbenv/ruby-build/pull/2576
Patch:          2576.patch

BuildRequires:  gawk
BuildRequires:  grep
%if %{with check}
BuildRequires:  bats
%endif

# ruby-build can build various ruby interpreters from source, which in turn can
# require additional dependencies
Recommends:     bzip2
Recommends:     clang
Recommends:     gdbm-devel
Recommends:     java-headless
Recommends:     libffi-devel
Recommends:     libyaml-devel
Recommends:     llvm-devel
Recommends:     make
Recommends:     ncurses-devel
Recommends:     openssl-devel
Recommends:     patch
Recommends:     perl-File-Compare
Recommends:     perl-FindBin
Recommends:     readline-devel
Recommends:     ruby
Recommends:     rubygem-rake
Recommends:     rust
Recommends:     zlib-devel

%description
ruby-build is a command-line utility that makes it easy to install virtually
any version of Ruby, from source.

%package        rbenv
Summary:        rbenv plugin to compile and install Ruby
Requires:       ruby-build = %{version}-%{release}
Requires:       rbenv

%description    rbenv
This package contains a plugin for rbenv that provides the "rbenv install"
command.

%prep
%autosetup -p1

%install
PREFIX=%{buildroot}%{_prefix} ./install.sh
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 share/man/man1/ruby-build.1

install -Ddpm0755 %{buildroot}%{_libdir}/rbenv/libexec
mv %{buildroot}%{_bindir}/rbenv-* %{buildroot}%{_libdir}/rbenv/libexec

%if %{with check}
%check
# Skip failing tests
for test in "install bundled OpenSSL on macOS"; do
  awk -i inplace '/^@test\s+"'"$test"'"\s*\{/{ print; print "  skip \"disabled failing test\""; next }1' $(grep -rl "@test \"$test\"")
done
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%files rbenv
%{_libdir}/rbenv/libexec/*

%changelog
%autochangelog
