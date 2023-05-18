%global forgeurl https://github.com/cvmfs/collectd-cvmfs

Name:           python-collectd_cvmfs
Version:        1.3.3
%global tag     %{version}
%forgemeta
Release:        %autorelease
Summary:        Collectd plugin to monitor CvmFS Clients

License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildArch:      noarch
 
BuildRequires:  python3-devel
# For import in checks
BuildRequires:  collectd-python

%global _description %{expand:
Collectd module for CvmFS clients. Reports time to mount as well as
other parameters vailable from the extended attributes of a CvmFS file
system.}

%description %_description

%package -n     python3-collectd_cvmfs
Summary:        %{summary}
Requires:       collectd-python

%description -n python3-collectd_cvmfs %_description


%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires  -t


%build
%pyproject_wheel


%install
%pyproject_install

mkdir -p %{buildroot}%{_datadir}/collectd
mv %{buildroot}%{python3_sitelib}%{_datadir}/collectd/collectd_cvmfs.db %{buildroot}%{_datadir}/collectd/collectd_cvmfs.db

%pyproject_save_files collectd_cvmfs


%check
%tox


%files -n python3-collectd_cvmfs -f %{pyproject_files}
%license LICENSE
%{_datadir}/collectd/collectd_cvmfs.db


%changelog
%autochangelog
