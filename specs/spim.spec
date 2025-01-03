Name:           spim
Version:        20230804
Release:        0.9.svn%{?dist}
Summary:        An assembly language MIPS32 simulator
License:        BSD-3-Clause
URL:            http://spimsimulator.sourceforge.net/

# These source files are generated from SPIM's Subversion repository.
#
# Run "svn co http://svn.code.sf.net/p/spimsimulator/code/ spimsimulator"
#     "cd spimsimulator"
# For each PROJECT: spim, CPU, and Documentation:
#     "tar czvf spimsimulator-[PROJECT]-[DATE].tar.gz [PROJECT]"
#
# The sources are taken from SVN because the upstream tarballs contain
# compiled code.
Source0:        spimsimulator-spim-20230804.tar.gz
Source1:        spimsimulator-CPU-20230804.tar.gz
Source2:        spimsimulator-Documentation-20230804.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++ flex bison

%description
spim is a self-contained simulator that runs MIPS32 programs. It reads and
executes assembly language programs written for this processor. spim also
provides a simple debugger and minimal set of operating system services.

%prep
%setup -q -T -a 0 -c
%setup -q -T -D -a 1 -c
%setup -q -T -D -a 2 -c -n spim-%{version}/spim

# Fix EOL encoding.
sed 's/\r//' README > README.unix
touch -r README README.unix
mv -f README.unix README

# Fix some permissions.
find . -type f -perm /0111 -print0 | xargs -0 chmod a-x

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 -D Documentation/spim.man %{buildroot}%{_mandir}/man1/spim.1

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%doc README

%changelog
* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230804-0.8.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230804-0.7.svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

%autochangelog
