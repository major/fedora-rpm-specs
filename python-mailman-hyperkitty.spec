Name:           python-mailman-hyperkitty
Version:        1.2.1
Release:        %autorelease
Summary:        Mailman archiver plugin for HyperKitty

License:        GPL-3.0-or-later
URL:            https://gitlab.com/mailman/mailman-hyperkitty/
Source:         %{pypi_source mailman-hyperkitty}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This package configures Mailman to send emails to HyperKitty for archiving.}

%description %_description

%package -n     python3-mailman-hyperkitty
Summary:        %{summary}

%description -n python3-mailman-hyperkitty %_description


%prep
%autosetup -p1 -n mailman-hyperkitty-%{version}


%generate_buildrequires
%pyproject_buildrequires %{!?el9:-t}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mailman_hyperkitty

# Mailman config file
install -D -m 644 mailman-hyperkitty.cfg \
    %{buildroot}%{_sysconfdir}/mailman3.d/hyperkitty.cfg


%check
%pyproject_check_import
%{!?el9:%tox}


%files -n python3-mailman-hyperkitty -f %{pyproject_files}
%config(noreplace) %{_sysconfdir}/mailman3.d/hyperkitty.cfg


%changelog
%autochangelog
