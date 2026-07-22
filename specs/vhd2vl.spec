Name:          vhd2vl
Version:       2.5
Release:       %autorelease
Summary:       VHDL to Verilog translator
License:       GPL-2.0-or-later
Url:           http://doolittle.icarus.com/~larry/vhd2vl/
Source0:       http://doolittle.icarus.com/~larry/%{name}/%{name}-%{version}.tar.gz
ExcludeArch:   %{ix86}
BuildRequires: make
BuildRequires: gcc
BuildRequires: flex bison flex-devel

%description
vhd2vl is a VHDL to Verilog translation program.
It targets the translation of synthetisable RTL.
While far from complete it supports a useful
subset of VHDL, sufficient for complex designs.


%prep
%autosetup

# rpmlint warning: W: wrong-file-end-of-line-encoding /usr/share/doc/vhd2vl-2.4/examples/gh_fifo_async16_sr.vhd
echo -n -e "... Fixing the end-of-line encodings of $f  \t"
sed -i.bak -e 's|\r||g' examples/gh_fifo_async16_sr.vhd
touch -r examples/gh_fifo_async16_sr.vhd.bak examples/gh_fifo_async16_sr.vhd
%{__rm} -f examples/gh_fifo_async16_sr.vhd.bak
echo "done"

%{__sed} -i "s|gcc \${STANDARD} \${WARNS} -O2 -g|gcc \${STANDARD} \${WARNS} %{optflags}|" src/makefile


%build
%make_build -C src


%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -pm 755 src/%{name} %{buildroot}%{_bindir}


%files
%{_bindir}/%{name}
%doc README.txt changes
%license GPLv2.txt
%doc examples translated_examples/


%changelog
%autochangelog
