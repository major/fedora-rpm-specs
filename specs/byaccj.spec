Summary:        Parser Generator with Java Extension
Name:           byaccj
Version:        1.15
Release:        %autorelease
License:        LicenseRef-Fedora-Public-Domain
URL:            http://byaccj.sourceforge.net/

Source0:        http://sourceforge.net/projects/byaccj/files/byaccj/1.15/byaccj1.15_src.tar.gz

Patch:          byaccj-c99.patch

BuildRequires:  gcc
BuildRequires:  make

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible 
parser generator. Standard YACC takes a YACC source file, and 
generates one or more C files from it, which if compiled properly, 
will produce a LALR-grammar parser. This is useful for expression 
parsing, interactive command parsing, and file reading. Many 
megabytes of YACC code have been written over the years.
This is the standard YACC tool that is in use every day to produce 
C/C++ parsers. I have added a "-J" flag which will cause BYACC to 
generate Java source code, instead. So there finally is a YACC for 
Java now! 

%prep
%autosetup -p1 -C
chmod -c -x src/* docs/*
sed -i -e 's|-arch i386 -isysroot /Developer/SDKs/MacOSX10.4u.sdk -mmacosx-version-min=10.4|$(LDFLAGS)|g' src/Makefile

%build
pushd src
%make_build yacc CFLAGS="%{optflags} -ansi" LDFLAGS="$RPM_LD_FLAGS"
popd

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 src/yacc %{buildroot}%{_bindir}/%{name}

%files
%doc docs/* src/README
%{_bindir}/%{name}

%changelog
%autochangelog
