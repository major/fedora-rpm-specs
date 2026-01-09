Name:           R-IRdisplay
Version:        %R_rpm_version 1.1
Release:        %autorelease
Summary:        'Jupyter' Display Machinery

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
 An interface to the rich display capabilities of 'Jupyter' front-ends
(e.g. 'Jupyter Notebook') <https://jupyter.org>. Designed to be used from a
running 'IRkernel' session <https://irkernel.github.io>.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
