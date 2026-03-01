Name:           kmodtool
Version:        1.2
Release:        %autorelease
Summary:        Tool for building kmod packages
License:        MIT
URL:            http://rpmfusion.org/Packaging/KernelModules/Kmods2
# We are upstream, these files are maintained directly in pkg-git
Source1:        %{name}-kmodtool
Source2:        %{name}-kernel-variants
Source3:        kmodtool-brp-kmodsign
Source4:        macros.kmodtool
BuildArch:      noarch


%description
This package contains tools and list of recent kernels that get used when
building kmod-packages.


%prep
# nothing to prep


%build
# nothing to build


%install
mkdir -p -m 0755 %{buildroot}%{_bindir} \
                 %{buildroot}%{_datadir}/%{name} \
                 %{buildroot}%{_rpmconfigdir} \
                 %{buildroot}%{_rpmmacrodir}
install -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/kmodtool
install -p -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/kernel-variants
install -p -m 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/brp-kmodsign
install -p -m 0644 %{SOURCE4} %{buildroot}%{_rpmmacrodir}/


%files
%{_bindir}/*
%{_datadir}/%{name}
%{_rpmconfigdir}/brp-kmodsign
%{_rpmmacrodir}/macros.kmodtool

%changelog
%autochangelog
