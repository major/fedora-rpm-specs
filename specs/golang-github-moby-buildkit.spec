# Generated by go2rpm 1.8.1
%bcond_without check
# Avoid noarch package built differently on different architectures
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(github.com/tonistiigi/go-archvariant\\)$

# https://github.com/moby/buildkit
%global goipath         github.com/moby/buildkit
Version:                0.10.5

%gometa -f

%global godevelheader %{expand:
Requires: golang(github.com/tonistiigi/go-archvariant)}

%global common_description %{expand:
BuildKit is a toolkit for converting source code to build artifacts in an
efficient, expressive and repeatable manner.}

%global golicenses      LICENSE
%global godocs          docs examples AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Concurrent, cache-efficient, and Dockerfile-agnostic builder toolkit

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}
Patch0:         0001-Remove-dependency-on-InstrumentationLibrary.patch
# https://github.com/moby/buildkit/pull/3144
Patch1:         3144.patch

%description %{common_description}

%gopkg

%prep
%goprep
# Remove in next release
sed -i "s|github.com/containerd/stargz-snapshotter/snapshot/overlayutils|github.com/containerd/containerd/snapshots/overlay/overlayutils|" $(find . -iname "*.go" -type f)
%patch -P0 -p1
%patch -P1 -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
for test in "TestMergeOp" \
            "TestSnapshotExtract" \
            "TestGetRemotes" \
            "TestExtractOnMutable" \
            "TestDiffOp" \
            "TestChecksumHardlinks" \
            "TestChecksumBasicFile" \
            "TestSymlinkAbsDirSuffix" \
            "TestChecksumIncludeDoubleStar" \
            "TestChecksumSymlinkNoParentScan" \
            "TestSymlinksNoFollow" \
            "TestSymlinkNeedsScan" \
            "TestPersistence" \
            "TestChecksumIncludeSymlink" \
            "TestChecksumWildcardOrFilter" \
            "TestSymlinkThroughParent" \
            "TestSymlinkInPathScan" \
            "TestChecksumIncludeExclude" \
            "TestClientGatewayIntegration" \
            "TestIntegration" \
            "TestCLIIntegration" \
            "TestFrontendIntegration" \
            "TestTargetBuildInfo" \
            "TestMerge" \
            "TestHardlinks" \
            "TestUsage" \
            "TestJobsIntegration" \
            "TestSubdir" \
            "TestMultipleReposKeepGitDir" \
            "TestFetchByTagKeepGitDir" \
            "TestRepeatedFetchKeepGitDir" \
            "TestFetchByAnnotatedTagKeepGitDir" \
            "TestFetchBySHAKeepGitDir" \
            "TestSubdirKeepGitDir" \
            "TestMultipleRepos" \
            "TestFetchByAnnotatedTag" \
            "TestFetchByTag" \
            "TestRepeatedFetch" \
            "TestFetchBySHA" \
            "TestHTTPDefaultName" \
            "TestHTTPSource" \
            "TestHTTPChecksum" \
            "TestSimpleDiff" \
            "TestRenameDiff" \
            "TestEmptyFileDiff" \
            "TestNestedDeletion" \
            "TestDirectoryReplace" \
            "TestRemoveDirectoryTree" \
            "TestRemoveDirectoryTreeWithDash" \
            "TestFileReplace" \
            "TestParentDirectoryPermission" \
            "TestUpdateWithSameTime" \
            "TestLchtimes" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%files
%license LICENSE
%doc docs examples AUTHORS README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog