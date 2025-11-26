Name:           nmon
Version:        16s
Release:        %autorelease
Summary:        Nigel's performance Monitor for Linux 

License:        GPL-3.0-only
URL:            https://nmon.sourceforge.io/
Source0:        https://sourceforge.net/projects/%{name}/files/lmon%{version}.c
Source1:        https://sourceforge.net/projects/%{name}/files/Documentation.txt
# Manpage available from the patch archive:
# http://sourceforge.net/tracker/?func=detail&aid=2833213&group_id=271307&atid=1153693
Source2:        %{name}.1

BuildRequires:  gcc
BuildRequires:  ncurses-devel


%description
nmon is a systems administrator, tuner, benchmark tool, which provides 
information about CPU, disks, network, etc., all in one view.


%prep
%setup -T -c -n %{name}
sed -e "s/\r//" %{SOURCE1} > Documentation.txt
touch -c -r %{SOURCE1} Documentation.txt
cp %{SOURCE0} .


%build
%ifarch %{arm32} %{arm64}
  %{__cc} %{optflags} -lncurses -lm lmon%{version}.c -o %{name} -D ARM
%elifarch s390 s390x
  %{__cc} %{optflags} -lncurses -lm lmon%{version}.c -o %{name} -D MAINFRAME
%elifarch ppc %{power64}
  %{__cc} %{optflags} -lncurses -lm lmon%{version}.c -o %{name} -D POWER
%elifarch %{ix86} x86_64
  %{__cc} %{optflags} -lncurses -lm lmon%{version}.c -o %{name} -D X86
%else
  %{__cc} %{optflags} -lncurses -lm lmon%{version}.c -o %{name}
%endif


%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/%{name}.1


%files
%doc Documentation.txt 
%{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}


%changelog
%autochangelog
