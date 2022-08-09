import matplotlib.pyplot as plt
import csv_read
import seaborn as sns

csv_read.read_data()

# raised_hands = csv_read.csv_data['raisedhands']
# discussion = csv_read.csv_data['Discussion']
# v_resources = csv_read.csv_data['VisitedResources']
# v_announcements = csv_read.csv_data['AnnouncementsView']


# def correlation(x, y):
#     std_x = (x-x.mean())/x.std(ddof=0)
#     std_y = (y-y.mean())/y.std(ddof=0)

#     return (std_x * std_y).mean()


# fig, ax = plt.subplots(figsize=(9, 7))
# sns.heatmap(csv_read.csv_data.corr(), annot=True)
# plt.show()

print(csv_read.csv_data)

Class = csv_read.csv_data['Class']
print(Class)
fig = plt.figure(figsize=(18, 8))
plt.subplot(221)
csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                 == 1].plot(kind='kde')
csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                 == 2].plot(kind='kde')
csv_read.csv_data['raisedhands'][csv_read.csv_data['Class']
                                 == 3].plot(kind='kde')
plt.legend(('1', '2', '3'), loc='best')
plt.title('Raised Hands')
plt.subplot(222)
csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                 == 1].plot(kind='kde')
csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                 == 2].plot(kind='kde')
csv_read.csv_data['VisitedResources'][csv_read.csv_data['Class']
                                 == 3].plot(kind='kde')
plt.legend(('1', '2', '3'), loc='best')
plt.title('VisitedResources')
plt.subplot(223)
csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                 == 1].plot(kind='kde')
csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                 == 2].plot(kind='kde')
csv_read.csv_data['AnnouncementsView'][csv_read.csv_data['Class']
                                 == 3].plot(kind='kde')
plt.legend(('1', '2', '3'), loc='best')
plt.title('AnnouncementsView')
plt.subplot(224)
csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                 == 1].plot(kind='kde')
csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                 == 2].plot(kind='kde')
csv_read.csv_data['Discussion'][csv_read.csv_data['Class']
                                 == 3].plot(kind='kde')
plt.legend(('1', '2', '3'), loc='best')
plt.title('Discussion')
plt.show()
