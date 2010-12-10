Summary: 	kio-bookmarks
Name: 		kio-bookmarks
Version: 	0.2.1
Release: 	%mkrel 3
Source:		http://kde-apps.org/CONTENT/content-files/86516-kio_bookmarks-%version.tgz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://kde-apps.org/content/show.php?content=86516
BuildRequires:  kdelibs4-devel

%description
kio_bookmarks is a new way to access your bookmarks. It displays them in an html
page you can use as your home page. No need to crawl in the bookmark menu, they
are all before you.

Features :
  - displays folders on multiple columns
  - displays favicons and folder icons

%files
%defattr(-,root,root)
%doc README TODO
%{_kde_libdir}/kde4/*.so
%{_kde_appsdir}/kio_bookmarks
%{_kde_services}/*

#--------------------------------------------------------------------

%prep
%setup -qn kio_bookmarks-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT
