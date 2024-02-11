Name:           msm-cros-efs-loader
Version:        1.0.2
Release:        %autorelease
Summary:        EFS loader for Qualcomm-based Chrome OS devices

License:        GPL-3.0-or-later
URL:            https://gitlab.com/postmarketOS/msm-cros-efs-loader

Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch

%description
EFS loader for Qualcomm-based Chrome OS devices

%prep
%autosetup -p1 -n %{name}-v%{version}

%install
install -D -p -m 0755 msm-cros-efs-loader.sh %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
