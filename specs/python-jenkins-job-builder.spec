%global pypi_name jenkins_job_builder

Name:           python-jenkins-job-builder
Version:        6.4.3
Release:        %autorelease
# Someone thought that 2.0.0.0b3 < 2.0.0
Epoch:          1
Summary:        Manage Jenkins jobs with YAML
License:        Apache-2.0
URL:            https://jenkins-job-builder.readthedocs.io/en/latest/
Source:         %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
# test-requirements.txt
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(testtools) >= 1.4

# Explicitly require a version of python3-jenkins that includes the patch from
# https://src.fedoraproject.org/rpms/python-jenkins/pull-request/1
Requires:       python3dist(python-jenkins) >= 1.8

%description
Jenkins Job Builder takes simple descriptions of Jenkins jobs in YAML format
and uses them to configure Jenkins. You can keep your job descriptions in
human readable text format in a version control system to make changes and
auditing easier. It also has a flexible template system, so creating many
similarly configured jobs is easy.

%prep
%autosetup -n %{pypi_name}-%{version}%{?pre} -p1
rm -vr *.egg-info/

%generate_buildrequires
%pyproject_buildrequires

%build
export PBR_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jenkins_jobs

%check
%pytest

%files -f %{pyproject_files}
%license LICENSE
%{_bindir}/jenkins-jobs

%changelog
%autochangelog
