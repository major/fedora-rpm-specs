Name:           nmon
Version:        16n
Release:        %autorelease
Summary:        Nigel's performance Monitor for Linux 

License:        GPLv3
URL:            http://nmon.sourceforge.net
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
%ifarch ppc %{power64}
  %{__cc} %{optflags} -D JFS -D GETUSER \
     -D LARGEMEM -lncurses -lm lmon%{version}.c -D POWER -o %{name}
%else
  %{__cc} %{optflags} -D JFS -D GETUSER \
     -D LARGEMEM -D X86 -lncurses -lm lmon%{version}.c -o %{name}
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
