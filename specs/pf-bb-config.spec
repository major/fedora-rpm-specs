Name:           pf-bb-config
Version:        25.11
Release:        %autorelease
Summary:        PF BBDEV (baseband device) Configuration Application

License:        Apache-2.0
URL:            https://github.com/intel/pf-bb-config
Source0:        %{url}/archive/v%{version}/pf-bb-config-%{version}.tar.gz

# Currently big endian is not supported due to a bug
ExcludeArch:    s390x

BuildRequires:  gcc
BuildRequires:  make


%description
The PF BBDEV (baseband device) Configuration Application "pf_bb_config"
provides a means to configure the baseband device at the host-level.
The program accesses the configuration space and sets the various parameters
through memory-mapped IO read/writes.


%prep
%autosetup -p1
sed -i "s/#VERSION_STRING#/%{version}/g" config_app.c


%build
%make_build CFLAGS="${RPM_OPT_FLAGS}" LDFLAGS="${RPM_LD_FLAGS}"


%install
for dir in acc100 agx100 fpga_5gnr fpga_lte vrb1 vrb2; do
	install -d -m 755 %{buildroot}%{_datadir}/pf-bb-config/$dir/
	cp -a $dir/*.cfg %{buildroot}%{_datadir}/pf-bb-config/$dir/
done
install -d -m 755 %{buildroot}%{_bindir}
install -p -D -m 755 pf_bb_config %{buildroot}%{_bindir}/pf_bb_config


%files
%license LICENSE
%doc README.md
%{_bindir}/pf_bb_config
%{_datadir}/pf-bb-config/


%autochangelog
