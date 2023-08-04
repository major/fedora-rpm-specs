%global debug_package %{nil}

Summary:	A GIF to PNG converter
Name:		gif2png
Version:	2.5.14
Release:	%autorelease
License:	BSD
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%name-%version.tar.gz
Source100:	test-0.gif
Source101:	test-1.gif
BuildRequires:  gcc
BuildRequires:	libpng-devel
BuildRequires:	make


%description
The gif2png program converts files from the obsolescent Graphic Interchange
Format to Portable Network Graphics. The conversion preserves all graphic
information, including transparency, perfectly. The gif2png program can
even recover data from corrupted GIFs.

There exists a 'web2png' program in a separate package which is able
to convert entire directory hierarchies.


%prep
%autosetup


%build
%make_build


%install
%make_install

# web2png is Python 2 only, see https://bugzilla.redhat.com/show_bug.cgi?id=1787242
rm %{buildroot}%{_bindir}/web2png
rm %{buildroot}%{_mandir}/man1/web2png*

#disable tests for while
#%check
#P=./gif2png
#for i in %SOURCE100 %SOURCE101; do
#    rm -f _tmp.gif
#    install -p -m 0644 $i _tmp.gif
#    $P _tmp.gif
#    $P -f < "$i" > _tmp.png
#    $P -O -f < "$i" > _tmp.png
#done


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*



%changelog
%autochangelog
