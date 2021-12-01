%define		kdeplasmaver	5.23.4
%define		qtver		5.9.0
%define		kpname		khotkeys

Summary:	Hot keys handling
Name:		kp5-%{kpname}
Version:	5.23.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	679e9b0049272f9dd09fd5aa196d4083
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-plasma-workspace-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Hot keys handling.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libkhotkeysprivate.so.5
%attr(755,root,root) %{_libdir}/libkhotkeysprivate.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_hotkeys.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/khotkeys.so
%{_datadir}/dbus-1/interfaces/org.kde.khotkeys.xml
%{_datadir}/khotkeys
%{_datadir}/kservices5/khotkeys.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KHotKeysDBusInterface
